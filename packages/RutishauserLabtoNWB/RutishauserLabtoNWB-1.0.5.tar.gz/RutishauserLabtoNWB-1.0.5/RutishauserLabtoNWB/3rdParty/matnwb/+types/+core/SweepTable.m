classdef SweepTable < types.core.DynamicTable
% SWEEPTABLE The table which groups different PatchClampSeries together.


% PROPERTIES
properties
    series; % The PatchClampSeries with the sweep number in that row
    series_index; % Index for series
    sweep_number; % The sweep number of the PatchClampSeries in that row.
end

methods
    function obj = SweepTable(varargin)
        % SWEEPTABLE Constructor for SweepTable
        %     obj = SWEEPTABLE(parentname1,parentvalue1,..,parentvalueN,parentargN,name1,value1,...,nameN,valueN)
        % series = VectorData
        % series_index = VectorIndex
        % sweep_number = VectorData
        varargin = [{'help' 'The table which groups different PatchClampSeries together'} varargin];
        obj = obj@types.core.DynamicTable(varargin{:});
        
        
        p = inputParser;
        p.KeepUnmatched = true;
        p.PartialMatching = false;
        p.StructExpand = false;
        addParameter(p, 'series',[]);
        addParameter(p, 'series_index',[]);
        addParameter(p, 'sweep_number',[]);
        parse(p, varargin{:});
        obj.series = p.Results.series;
        obj.series_index = p.Results.series_index;
        obj.sweep_number = p.Results.sweep_number;
        if strcmp(class(obj), 'types.core.SweepTable')
            types.util.checkUnset(obj, unique(varargin(1:2:end)));
        end
    end
    %% SETTERS
    function obj = set.series(obj, val)
        obj.series = obj.validate_series(val);
    end
    function obj = set.series_index(obj, val)
        obj.series_index = obj.validate_series_index(val);
    end
    function obj = set.sweep_number(obj, val)
        obj.sweep_number = obj.validate_sweep_number(val);
    end
    %% VALIDATORS
    
    function val = validate_series(obj, val)
        val = types.util.checkDtype('series', 'types.core.VectorData', val);
    end
    function val = validate_series_index(obj, val)
        val = types.util.checkDtype('series_index', 'types.core.VectorIndex', val);
    end
    function val = validate_sweep_number(obj, val)
        val = types.util.checkDtype('sweep_number', 'types.core.VectorData', val);
    end
    %% EXPORT
    function refs = export(obj, fid, fullpath, refs)
        refs = export@types.core.DynamicTable(obj, fid, fullpath, refs);
        if any(strcmp(refs, fullpath))
            return;
        end
        if ~isempty(obj.series)
            refs = obj.series.export(fid, [fullpath '/series'], refs);
        else
            error('Property `series` is required.');
        end
        if ~isempty(obj.series_index)
            refs = obj.series_index.export(fid, [fullpath '/series_index'], refs);
        else
            error('Property `series_index` is required.');
        end
        if ~isempty(obj.sweep_number)
            refs = obj.sweep_number.export(fid, [fullpath '/sweep_number'], refs);
        else
            error('Property `sweep_number` is required.');
        end
    end
end

end