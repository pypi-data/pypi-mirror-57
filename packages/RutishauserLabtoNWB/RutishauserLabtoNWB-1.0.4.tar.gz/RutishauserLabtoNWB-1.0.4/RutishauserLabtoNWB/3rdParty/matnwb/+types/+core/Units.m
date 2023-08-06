classdef Units < types.core.DynamicTable
% UNITS Data about spiking units. Event times of observed units (e.g. cell, synapse, etc.) should be concatenated and stored in spike_times.


% PROPERTIES
properties
    electrode_group; % the electrode group that each spike unit came from
    electrodes; % the electrode that each spike unit came from
    electrodes_index; % the index into electrodes
    obs_intervals; % the observation intervals for each unit
    obs_intervals_index; % the index into the obs_intervals dataset
    spike_times; % the spike times for each unit
    spike_times_index; % the index into the spike_times dataset
    waveform_mean; % the spike waveform mean for each spike unit
    waveform_sd; % the spike waveform standard deviation for each spike unit
end

methods
    function obj = Units(varargin)
        % UNITS Constructor for Units
        %     obj = UNITS(parentname1,parentvalue1,..,parentvalueN,parentargN,name1,value1,...,nameN,valueN)
        % electrode_group = VectorData
        % electrodes = DynamicTableRegion
        % electrodes_index = VectorIndex
        % obs_intervals = VectorData
        % obs_intervals_index = VectorIndex
        % spike_times = VectorData
        % spike_times_index = VectorIndex
        % waveform_mean = VectorData
        % waveform_sd = VectorData
        varargin = [{'help' 'Data about spiking units'} varargin];
        obj = obj@types.core.DynamicTable(varargin{:});
        
        
        p = inputParser;
        p.KeepUnmatched = true;
        p.PartialMatching = false;
        p.StructExpand = false;
        addParameter(p, 'electrode_group',[]);
        addParameter(p, 'electrodes',[]);
        addParameter(p, 'electrodes_index',[]);
        addParameter(p, 'obs_intervals',[]);
        addParameter(p, 'obs_intervals_index',[]);
        addParameter(p, 'spike_times',[]);
        addParameter(p, 'spike_times_index',[]);
        addParameter(p, 'waveform_mean',[]);
        addParameter(p, 'waveform_sd',[]);
        parse(p, varargin{:});
        obj.electrode_group = p.Results.electrode_group;
        obj.electrodes = p.Results.electrodes;
        obj.electrodes_index = p.Results.electrodes_index;
        obj.obs_intervals = p.Results.obs_intervals;
        obj.obs_intervals_index = p.Results.obs_intervals_index;
        obj.spike_times = p.Results.spike_times;
        obj.spike_times_index = p.Results.spike_times_index;
        obj.waveform_mean = p.Results.waveform_mean;
        obj.waveform_sd = p.Results.waveform_sd;
        if strcmp(class(obj), 'types.core.Units')
            types.util.checkUnset(obj, unique(varargin(1:2:end)));
        end
    end
    %% SETTERS
    function obj = set.electrode_group(obj, val)
        obj.electrode_group = obj.validate_electrode_group(val);
    end
    function obj = set.electrodes(obj, val)
        obj.electrodes = obj.validate_electrodes(val);
    end
    function obj = set.electrodes_index(obj, val)
        obj.electrodes_index = obj.validate_electrodes_index(val);
    end
    function obj = set.obs_intervals(obj, val)
        obj.obs_intervals = obj.validate_obs_intervals(val);
    end
    function obj = set.obs_intervals_index(obj, val)
        obj.obs_intervals_index = obj.validate_obs_intervals_index(val);
    end
    function obj = set.spike_times(obj, val)
        obj.spike_times = obj.validate_spike_times(val);
    end
    function obj = set.spike_times_index(obj, val)
        obj.spike_times_index = obj.validate_spike_times_index(val);
    end
    function obj = set.waveform_mean(obj, val)
        obj.waveform_mean = obj.validate_waveform_mean(val);
    end
    function obj = set.waveform_sd(obj, val)
        obj.waveform_sd = obj.validate_waveform_sd(val);
    end
    %% VALIDATORS
    
    function val = validate_electrode_group(obj, val)
        val = types.util.checkDtype('electrode_group', 'types.core.VectorData', val);
    end
    function val = validate_electrodes(obj, val)
        val = types.util.checkDtype('electrodes', 'types.core.DynamicTableRegion', val);
    end
    function val = validate_electrodes_index(obj, val)
        val = types.util.checkDtype('electrodes_index', 'types.core.VectorIndex', val);
    end
    function val = validate_obs_intervals(obj, val)
        val = types.util.checkDtype('obs_intervals', 'types.core.VectorData', val);
    end
    function val = validate_obs_intervals_index(obj, val)
        val = types.util.checkDtype('obs_intervals_index', 'types.core.VectorIndex', val);
    end
    function val = validate_spike_times(obj, val)
        val = types.util.checkDtype('spike_times', 'types.core.VectorData', val);
    end
    function val = validate_spike_times_index(obj, val)
        val = types.util.checkDtype('spike_times_index', 'types.core.VectorIndex', val);
    end
    function val = validate_waveform_mean(obj, val)
        val = types.util.checkDtype('waveform_mean', 'types.core.VectorData', val);
    end
    function val = validate_waveform_sd(obj, val)
        val = types.util.checkDtype('waveform_sd', 'types.core.VectorData', val);
    end
    %% EXPORT
    function refs = export(obj, fid, fullpath, refs)
        refs = export@types.core.DynamicTable(obj, fid, fullpath, refs);
        if any(strcmp(refs, fullpath))
            return;
        end
        if ~isempty(obj.electrode_group)
            refs = obj.electrode_group.export(fid, [fullpath '/electrode_group'], refs);
        end
        if ~isempty(obj.electrodes)
            refs = obj.electrodes.export(fid, [fullpath '/electrodes'], refs);
        end
        if ~isempty(obj.electrodes_index)
            refs = obj.electrodes_index.export(fid, [fullpath '/electrodes_index'], refs);
        end
        if ~isempty(obj.obs_intervals)
            refs = obj.obs_intervals.export(fid, [fullpath '/obs_intervals'], refs);
        end
        if ~isempty(obj.obs_intervals_index)
            refs = obj.obs_intervals_index.export(fid, [fullpath '/obs_intervals_index'], refs);
        end
        if ~isempty(obj.spike_times)
            refs = obj.spike_times.export(fid, [fullpath '/spike_times'], refs);
        end
        if ~isempty(obj.spike_times_index)
            refs = obj.spike_times_index.export(fid, [fullpath '/spike_times_index'], refs);
        end
        if ~isempty(obj.waveform_mean)
            refs = obj.waveform_mean.export(fid, [fullpath '/waveform_mean'], refs);
        end
        if ~isempty(obj.waveform_sd)
            refs = obj.waveform_sd.export(fid, [fullpath '/waveform_sd'], refs);
        end
    end
end

end