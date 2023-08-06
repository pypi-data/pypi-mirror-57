"""Provide alarm management.
"""
import sys
import collections
import datetime
import logging
log = logging.getLogger('msiempy')

from . import NitroDict, NitroList, FilteredQueryList
from .event import EventManager, Event
from .__utils__ import regex_match, convert_to_time_obj, dehexify


__pdoc__={}

class AlarmManager(FilteredQueryList):
    """
    Interface to query and manage Alarms.  
    Inherits from `msiempy.FilteredQueryList`.

    Arguments:  

    - `status_filter` : status of the alarms to query. `status_filter` is not a filter like other cause it's computed on the SIEM side.  
    Accepted values : `acknowledged`, `unacknowledged`, `all`, `` or `None` (default is ``).
    `filters` are computed locally - Unlike `msiempy.event.EventManager` filters.  
    - `page_size` : max number of rows per query.  
    - `page_number` : defaulted to 1.
    - `filters` : `[(field, [values]), (field, [values])]` Filters applied to `msiempy.alarm.Alarm` objects. A single `tuple` is also accepted.  
    - `event_filters` : `[(field, [values]), (field, [values])]` Filters applied to `msiempy.event.Event` objects. A single `tuple` is also accepted.  
    - `time_range` : Query time range. String representation of a time range.  
    - `start_time` : Query starting time, can be a `string` or a `datetime` object. Parsed with `dateutil`.  
    - `end_time` : Query endding time, can be a `string` or a `datetime` object. Parsed with `dateutil`.  
    - `load_async` : Load asynchonously the sub-queries. Defaulted to `True`.  
    
    """
    def __init__(self, *args, status_filter='all', page_size=200, filters=None, event_filters=None, **kwargs):
        super().__init__(*args, **kwargs)

        #Declaring attributes
        self._alarm_filters = list(tuple())
        self._event_filters = list(tuple())
        self._status_filter = str()

        #Setting attributes
        self.status_filter=status_filter
        self.page_size=page_size

        #uses the parent filter setter
        #TODO : find a soltuion not to use this
        #callign super().filters=filters #https://bugs.python.org/issue14965
        super(self.__class__, self.__class__).filters.__set__(self, filters)

        #Seeting events filters after alarms filters cause it would overwrite it
        self.event_filters=event_filters

        #Casting all data to Alarms objects, better way to do it ?
        collections.UserList.__init__(self, [Alarm(adict=item) for item in self.data if isinstance(item, (dict, NitroDict))])

    

    @property
    def filters(self):
        """
        Returns the alarm related filters
        """
        return self._alarm_filters
    
    @property
    def status_filter(self):
        """
        Status of the alarms in the query.  
        """
        return self._status_filter

    @status_filter.setter
    def status_filter(self, status_filter):
        status_found=False
        if type(status_filter) is str : 
            for synonims in Alarm.POSSIBLE_ALARM_STATUS :
                if status_filter in synonims:
                    self._status_filter=synonims[0]
                    status_found=True

        #Patch weird bug regarding paging : 
        if isinstance(status_filter, list) : #this is the patch
            self._status_filter='all'
            status_found=True 

        if not status_found:
            raise AttributeError("Illegal value of status filter. The status must be in "+str(Alarm.POSSIBLE_ALARM_STATUS)+' not :'+str(status_filter))

    def add_filter(self, afilter):
        """
        Make sure the filters format is `tuple(field, list(values in string))`.  
        
        Arguments :  

        - `afilter` : Can be a `tuple` (field,[values]) or `str` 'field=value'
        """

        if isinstance(afilter,str): afilter = afilter.split('=',1)
        
        values = afilter[1] if isinstance(afilter[1], list) else [afilter[1]]
        values = [str(v) for v in values]
        added=False

        for synonims in Alarm.ALARM_EVENT_FILTER_FIELDS :
            if afilter[0] in synonims :
                log.warning('Passing event related filters in `filters` argument is not safe consider using `event_filters` argument. You\'ll be able to use more filters dynamically.')
                self._event_filters.append((synonims[0], values))
                added=True

        #support query related filtering if the filter's field is composed by a table name then a field name separated by a dot.
        if len(afilter[0].split('.')) == 2 :
            self._event_filters.append((afilter[0], values))
            log.warning('Passing event related filters in `filters` argument is not safe, consider using `event_filters` argument. You\'ll be able to use more filters dynamically.')
            added=True

        if added==False:
            self._alarm_filters.append((afilter[0], values))
            added=True

       

    @property
    def event_filters(self):
        """Event related filters."""
        return self._event_filters

    @event_filters.setter
    def event_filters(self, filters):
        if isinstance(filters, list):
            for f in filters :
                self.add_event_filter(f)

        elif isinstance(filters, tuple):
            self.add_event_filter(filters)

        elif filters == None :
            self._event_filters=list(tuple())
        
        else :
            raise AttributeError("Illegal type for the filter object, it must be a list, a tuple or None.")

    def add_event_filter(self, afilter):
        """
        Make sure the filters format is `tuple(field, list(values in string))`.  

        Arguments :  

        - `afilter` : Can be a `tuple` (field,[values]) or `str` 'field=value'
        """

        if isinstance(afilter,str):
            afilter = afilter.split('=',1)
       
        values = afilter[1] if isinstance(afilter[1], list) else [afilter[1]]
        values = [str(v) for v in values] 
        self._event_filters.append((afilter[0], values))

    def clear_filters(self):
        """
        Reset local alarm and event filters.
        """
        self._alarm_filters = list(tuple())
        self._event_filters = list(tuple())

    def load_data(self, pages=1, **kwargs):
        """
        Implements automatic paging over `msiempy.alarm.AlarmManager.qry_load_data`.  
        
        Arguments :  

        - `pages` : Automatic pagging count (not asynchronous).   

        Arguments to `msiempy.alarm.AlarmManager.qry_load_data` :  

        - `workers` : Number of asynchronous workers   
        - `alarms_details` : Load detailed alarms infos. If `False`, only a couple values are loaded, no `events` infos.  
        - `events_details` : Load detailed events infos. If `False`, no detailed `events` will be loaded only `str` representation.  
        - `use_query` : Uses the query module to retreive event data. Only works with SIEM v11.2.1 or greater.  
        - `extra_fields` :  Only when `use_query=True`. Additionnal event fields to load in the query. See : `msiempy.event.EventManager`  
        - `page_number` : Page number, default to 1. Do not touch if you're using `pages` parameter  

        Returns : `msiempy.alarm.AlarmManager`
        """

        items, completed = self.qry_load_data(**kwargs)
        #Casting items to Alarms
        alarms=[Alarm(adict=item) for item in items]

        #Iterative automatic paging (not asynchronous)
        if not completed and pages>1 :
            next_kwargs={**kwargs}
            if 'page_number' in kwargs : next_kwargs['page_number']=kwargs['page_number']+1
            else: next_kwargs['page_number']=2

            log.info('Loading pages... ({})'.format(next_kwargs['page_number']))
            alarms=alarms+list(self.load_data(pages=pages-1, **next_kwargs))

        self.data=alarms

        if 'page_number' not in kwargs:
            log.info(str(len(alarms)) + " alarms are matching your filter(s)")

        return(self)

    def qry_load_data(self, workers=10,
        alarms_details=True, events_details=True,
        use_query=False, extra_fields=[], page_number=1):
        """
        Method that loads the alarms data :  
        -> Fetch the list of alarms and load alarms details  
        -> Filter depending on alarms related filters  
        -> Load the events details  
        -> Filter depending on event related filters  

        Arguments :  

        - `workers` : Number of asynchronous workers  
        - `alarms_details` : Load detailed alarms infos. If `False`, only a couple values are loaded, no `events` infos.
        - `events_details` : Load detailed events infos. If `False`, no detailed `events` will be loaded only `str` representation.
        - `use_query` : Uses the query module to retreive event data. Only works with SIEM v11.2.1 or greater.  
        - `extra_fields` :  Only when `use_query=True`. Additionnal event fields to load in the query. See : `msiempy.event.EventManager`  
        - `page_number` : Page number, default to 1. Do not touch if you're using `pages` parameter  
        
        Returns : `tuple` : ( Results : `list` , Status of the query : `completed` )

        """

        if self.time_range == 'CUSTOM' :
            no_filtered_alarms=self.nitro.request(
                'get_alarms_custom_time',
                time_range=self.time_range,
                start_time=self.start_time,
                end_time=self.end_time,
                status=self.status_filter,
                page_size=self.page_size,
                page_number=page_number
                )

        else :
            no_filtered_alarms=self.nitro.request(
                'get_alarms',
                time_range=self.time_range,
                status=self.status_filter,
                page_size=self.page_size,
                page_number=page_number
                )

        #Casting to list of Alarms to be able to call load_details etc...        
        alarm_based_filtered = [Alarm(adict=a) for a in no_filtered_alarms if self._alarm_match(a)]

        if alarms_details :

            log.info("Getting alarms infos...")
            alarm_detailed = self.perform(Alarm.load_details,
                list(alarm_based_filtered),
                asynch=True,
                progress=True,
                workers=workers)

            #Casting to list of Alarms to be able to call load_details etc...        
            detailed_alarm_based_filtered = [Alarm(adict=a) for a in alarm_detailed if self._alarm_match(a)]

            if events_details :
                log.info("Getting events infos...")
                event_detailed = self.perform(Alarm.load_events, 
                    list(alarm_detailed),
                    func_args=dict(use_query=use_query, extra_fields=extra_fields),
                    asynch=True, 
                    progress=True, 
                    workers=workers)

                filtered_alarms = [a for a in event_detailed if self._event_match(a)]
            else:
                log.warning('Field based Event filters are ignored when `events_details is False`. You can use `events` keyword in alarms filters to match str representation.')
                filtered_alarms=detailed_alarm_based_filtered
        else :
            filtered_alarms = alarm_based_filtered
            log.warning('Event filters and some Alarm filters are ignored when `alarms_details is False`')

        return (( filtered_alarms , len(no_filtered_alarms) < int(self.page_size) ))

    def _alarm_match(self, alarm):
        """
        Internal filter method that is going to return True if the passed alarm match any alarm related filters.
        """
        match=True
        for alarm_filter in self._alarm_filters :
            match=False
            if alarm_filter[0] not in alarm:
                break
            value = str(alarm[alarm_filter[0]]) #Can only match strings
            for filter_value in alarm_filter[1]:
                if regex_match(filter_value.lower(), value.lower()):
                    match=True
                    break
            if not match :
                break
        return match
        
    def _event_match(self, alarm):
        """
        Internal filter method that is going to return True if the passed alarm match any event related filters.
        """
        match=True
        for event_filter in self._event_filters :
            match=False
            if event_filter[0] not in alarm['events'][0]:
                break
            value = str(alarm['events'][0][event_filter[0]])
            for filter_value in event_filter[1]:
                if regex_match(filter_value.lower(), value.lower()) :
                    match=True
                    break
            if not match :
                break
        return match
        
class Alarm(NitroDict):
    """
    Dict keys :  

    - `id` : The ID of the triggered alarm  
    - `summary`  : The summary of the triggered alarm  
    - `assignee` : The assignee for this triggered alarm  
    - `severity` : The severity for this triggered alarm  
    - `triggeredDate` : The date this alarm was triggered  
    - `acknowledgedDate` : The date this triggered alarm was acknowledged  
    - `acknowledgedUsername` : The user that acknowledged this triggered alarm  
    - `alarmName` : The name of the alarm that was triggered  
    - `events` : The events for this user  
    - And others...  
    
    Arguments:

    - `adict`: Alarm parameters  
    - `id`: The alarm ID to instanciate. Will load informations
    """

    def __init__(self, *arg, **kwargs):
        """Creates a empty Alarm.
        """
        super().__init__(*arg, **kwargs)

        #Keep the id in the dict when instanciating an Alarm directly from its id.
        if 'id' in kwargs :
            self.data['id'] = {'value':str(kwargs['id'])}

    POSSIBLE_ALARM_STATUS=[
        ['acknowledged', 'ack',],
        ['unacknowledged', 'unack',],
        ['', 'all', 'both']
    ]
    __pdoc__['Alarm.POSSIBLE_ALARM_STATUS']="""Possible alarm statuses : ```%(statuses)s```""" % dict(statuses=', '.join([ '/'.join(synonims) for synonims in POSSIBLE_ALARM_STATUS]))

    ALARM_EVENT_FILTER_FIELDS=[
    ("ruleName",),
    ("srcIp",),
    ("destIp",),
    ("protocol",),
    ("lastTime",),
    ("subtype",),
    ("destPort",),
    ("destMac",),
    ("srcMac",),
    ("srcPort",),
    ("deviceName",),
    ("sigId",),
    ("normId",),
    ("srcUser",),
    ("destUser",),
    ("normMessage",),
    ("normDesc",),
    ("host",),
    ("domain",),
    ("ipsId",),
    ]
    __pdoc__['Alarm.ALARM_EVENT_FILTER_FIELDS']="""Static event related fields usable in a filter. Usable in `filters` parameter : ```%(fields)s```""" % dict(fields=', '.join([ '/'.join(synonims) for synonims in ALARM_EVENT_FILTER_FIELDS]))

    ALARM_DEFAULT_FIELDS=['id','alarmName', 'summary','triggeredDate', 'acknowledgedUsername']
    __pdoc__['Alarm.ALARM_DEFAULT_FIELDS']="""Defaulfs fields : `%(fields)s` 
    (not used , may be for printing with `msiempy.NitroList.get_text(fields=msiempy.alarm.ALARM_DEFAULT_FIELDS)`)""" % dict(fields=', '.join(ALARM_DEFAULT_FIELDS))


    def acknowledge(self):
        """Mark the alarm as acknowledged.
        """
        if self.nitro.api_v == 1:
            self.nitro.request('ack_alarms', ids=self.data['id']['value'])
        else:
            self.nitro.request('ack_alarms_11_2_1', ids=self.data['id']['value'])

    def unacknowledge(self):
        """Mark the alarm as unacknowledge.
        """
        if self.nitro.api_v == 1:
            self.nitro.request('unack_alarms', ids=self.data['id']['value'])
        else:
            self.nitro.request('unack_alarms_11_2_1', ids=self.data['id']['value'])


    def delete(self):
        """Destructive action!
        Delete the alarm.
        """
        if self.nitro.api_v == 1:
            self.nitro.request('delete_alarms', ids=self.data['id']['value'])
        else:
            self.nitro.request('delete_alarms_11_2_1', ids=self.data['id']['value'])

    def ceate_case(self):
        """Not implemented : TODO
        """
        raise NotImplementedError()

    def load_details(self):
        """Update the alarm with detailled data loaded from the SIEM.
        """
        the_id = self.data['id']['value']
        self.data.update(self.data_from_id(the_id))
        self.data['id']['value']=the_id

        return self

    def refresh(self):
        """Update the alarm with detailled data loaded from the SIEM.  
        """        
        self.load_details()

    def load_events(self, use_query=False, extra_fields=[]):
        """
        Retreive the genuine Event object from an Alarm.
        Warning : This method will only load the details of the first triggering event.  

        Arguments:  

        - `use_query` : Uses the query module to retreive common event data. Only works with SIEM v 11.2.x.  
        - `extra_fields` : Only when `use_query=True`. Additionnal event fields to load in the query. See : `msiempy.event.EventManager`  
        """
        if isinstance(self.data['events'], str):

            #Retreive the alert id from the event's string
            events_data=self.data['events'].split('|')
            the_id = events_data[0]+'|'+events_data[1]

            #instanciate the event
            the_first_event=Event()
            the_first_event.data = Event().data_from_id(id=the_id, use_query=use_query, extra_fields=extra_fields)

            #set it as the only item of the event list
            self.data['events']= [ the_first_event ]

        else:
            log.info('The alarm {} ({}) has no events associated'.format(self.data['alarmName'], self.data['triggeredDate']))
            self.data['events']= [ Event() ]

        return self

    def map_alarm_int_fields(self, alarm_details):
        """Map the internal ESM field names to msiempy style"""

        for key, val in alarm_details.items():
            if alarm_details[key] == key:
                alarm_details[key] = None
            elif alarm_details[key] in ['f', 'F']:
                alarm_details[key] = False
            elif alarm_details[key] in ['t', 'T']:
                alarm_details[key] = True
            else:
                alarm_details[key] = val

        new_alarm = {}
        new_alarm['filters'] = alarm_details.get('FILTERS') or None
        new_alarm['queryId'] = alarm_details.get('QID') or None
        new_alarm['alretRateMin'] = alarm_details.get('ARM') or None
        new_alarm['alertRateCount'] = alarm_details.get('ARC') or None
        new_alarm['percentAbove'] = alarm_details.get('PCTA') or None
        new_alarm['percentBelow'] = alarm_details.get('PCTB') or None
        new_alarm['offsetMinutes'] = alarm_details.get('OFFSETMIN') or None
        new_alarm['maximumConditionTriggerFrequency'] = alarm_details.get('TIMEF') or None
        new_alarm['useWatchlist'] = alarm_details.get('USEW') or None
        new_alarm['matchField'] = alarm_details.get('MFLD') or None
        new_alarm['matchValue'] = alarm_details.get('MWAL') or None
        #new_alarm['healthMonalarm_details'] = alarm_details.get('HMS') or None
        new_alarm['assigneeId'] = alarm_details.get('ASNID') or None
        new_alarm['escalatedDate'] = alarm_details.get('ESCDATE') or None
        new_alarm['caseId'] = alarm_details.get('CASEID') or None
        new_alarm['caseName'] = alarm_details.get('CASENAME') or None
        new_alarm['iocName'] = alarm_details.get('IOCNAME') or None
        new_alarm['iocId'] = alarm_details.get('IOCID') or None
        new_alarm['description'] = alarm_details.get('DESC') or None
        new_alarm['actions'] = alarm_details.get('ACTIONS') or None
        new_alarm['events'] = alarm_details.get('EVENTS') or None
        return new_alarm
                                                                                       
    def data_from_id(self, id):
        """
        Gets the alarm parameters based on an ID
        """
        alarms = self.nitro.request('get_alarm_details_int', id=str(id))
        alarms = {key: dehexify(val).replace('\n', '|') for key, val in alarms.items()} #this line is skechy
        alarms = self.map_alarm_int_fields(alarms)        
        return alarms
