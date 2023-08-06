classdef DynamicTableRegion < types.core.VectorData
% DYNAMICTABLEREGION a region/index into a DynamicTable


% PROPERTIES
properties
    table; % a reference to the DynamicTable this region applies to
end

methods
    function obj = DynamicTableRegion(varargin)
        % DYNAMICTABLEREGION Constructor for DynamicTableRegion
        %     obj = DYNAMICTABLEREGION(parentname1,parentvalue1,..,parentvalueN,parentargN,name1,value1,...,nameN,valueN)
        % table = ref to DynamicTable object
        varargin = [{'help' 'a subset (i.e. slice or region) of a DynamicTable'} varargin];
        obj = obj@types.core.VectorData(varargin{:});
        
        
        p = inputParser;
        p.KeepUnmatched = true;
        p.PartialMatching = false;
        p.StructExpand = false;
        addParameter(p, 'table',[]);
        parse(p, varargin{:});
        obj.table = p.Results.table;
        if strcmp(class(obj), 'types.core.DynamicTableRegion')
            types.util.checkUnset(obj, unique(varargin(1:2:end)));
        end
    end
    %% SETTERS
    function obj = set.table(obj, val)
        obj.table = obj.validate_table(val);
    end
    %% VALIDATORS
    
    function val = validate_data(obj, val)
        val = types.util.checkDtype('data', 'int', val);
    end
    function val = validate_description(obj, val)
        val = types.util.checkDtype('description', 'char', val);
    end
    function val = validate_table(obj, val)
        % Reference to type `DynamicTable`
        val = types.util.checkDtype('table', 'types.untyped.ObjectView', val);
    end
    %% EXPORT
    function refs = export(obj, fid, fullpath, refs)
        refs = export@types.core.VectorData(obj, fid, fullpath, refs);
        if any(strcmp(refs, fullpath))
            return;
        end
        if ~isempty(obj.table)
            io.writeAttribute(fid, [fullpath '/table'], class(obj.table), obj.table, false);
        else
            error('Property `table` is required.');
        end
    end
end

end