%Set up query

Start   = '<START DATE>'; %//Example: '2018-06-03'
End     = '<END DATE>'; %//Example: 2018-06-04
tsID    = '<DATA POINT ID'; %//Example: bacnet100-4120-CO2
prjct_id = '<PROJECT ID>'; %//Example: prjct_id = '17' You don't know your project ID? Consult the endpoint https://api.aedifion.io/ui/#!/User/get_user_projects to get the IDs of all your projects.

%get data
% authenticate whether via your login credentials or via token
TS = queryTimeseriesAedifion( Start, End, tsID, prjct_id);


%resample data
TS_sec = resample(TS, [(TS.TimeInfo.Start+1/(24*60*60))...
    :1/(24*60*60):TS.TimeInfo.End],'zoh');

% display observation times
Times = get(TS, 'Time');
datestr(Times(:))

% display resampled times
Times = get(TS_sec, 'Time');
datestr(Times(:))

