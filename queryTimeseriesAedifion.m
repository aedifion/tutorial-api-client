function [ data_timeseries ] = queryTimeseriesAedifion( Start, End, tsID, prjct_id )
%% This function queries the aedifion API and provides a timeseries of a 
% datapoint. View the documentation of this endpoint on https://api.aedifion.io/ui/#!/Datapoint/get_datapoint_timeseries
% To use the function, please define the API server and weboptions in your
% current workspace. 

%% Input:
%
%	Start:  Start date of data to be queried
%           type: string ('yyyy-mm-dd'), ('yyyy-mm-dd HH:MM:SS')
%	End:    End date of data to be queried
%           type: string ('yyyy-mm-dd'), ('yyyy-mm-dd HH:MM:SS')
%	tsID:	Database ID of queried data.
%           type: string ('ID')


%% Output:
%
%	data_timeseries:	Timeseries-object of data.
%						type: timeseries-object


%% configuration
% get api configuration
srvr = 'https://api.aedifion.io'; %//Default: srvr = 'https://api.aedifion.io';
email = input('Please insert your email address (or token from https://api.aedifion.io/ui/#!/User/get_token): ','s');
passwd = input('Please insert your password (if using token, please leave empty: ','s');
optns = weboptions('Username',email,'Password',passwd);

api_query = '/v2/datapoint/timeseries';


input_timestamp_start = ['start=',Start];
input_timestamp_end = ['end=',End];
input_timestamp_lastBefore = ['end=',Start];
number_values_lastBefore = ['max=','1'];

input_datapointID = ['dataPointID=',tsID];

if datenum(Start) >= datenum(End)
    error('End cannot be earlier than Start.');
else
    
    tsLastBefore = webread([srvr,api_query,'?project_id=',prjct_id,'&',input_datapointID,'&',...
        input_timestamp_lastBefore,'&',number_values_lastBefore],optns);
    
    tsEvent = webread([srvr,api_query,'?project_id=',prjct_id,'&',...
        input_datapointID,'&',input_timestamp_start,'&',input_timestamp_end],optns);
    
    if isempty(tsEvent.data) % Catch case if there is no data observed within time interval
        zoh_last_observation_value = tsLastBefore.data.value; 
        zoh_last_observation_time = datenum(End);
        
        data_timeseries = timeseries([tsLastBefore.data.value;...
            zoh_last_observation_value],[datenum(Start);...
            zoh_last_observation_time]);
        
    else
       	values = [tsEvent.data.value]';
        time_utcstr = {tsEvent.data.time}';
        time_matlab = datenum(strrep(strrep(time_utcstr,'Z',' '),'T',' '));
    
        zoh_last_observation_value = values(end); %get last value
        zoh_last_observation_time = datenum(End); %get last time
        
        data_timeseries = timeseries([tsLastBefore.data.value;values;...
            zoh_last_observation_value],[datenum(Start);time_matlab;...
            zoh_last_observation_time]); %append last value and last time 
    end

end
end
