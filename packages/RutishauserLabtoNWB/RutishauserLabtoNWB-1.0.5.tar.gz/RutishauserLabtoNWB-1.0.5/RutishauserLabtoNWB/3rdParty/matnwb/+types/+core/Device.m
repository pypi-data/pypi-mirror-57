classdef Device < types.core.NWBContainer
% DEVICE One of possibly many. Information about device and device description.



methods
    function obj = Device(varargin)
        % DEVICE Constructor for Device
        %     obj = DEVICE(parentname1,parentvalue1,..,parentvalueN,parentargN,name1,value1,...,nameN,valueN)
        varargin = [{'help' 'A recording device e.g. amplifier'} varargin];
        obj = obj@types.core.NWBContainer(varargin{:});
        if strcmp(class(obj), 'types.core.Device')
            types.util.checkUnset(obj, unique(varargin(1:2:end)));
        end
    end
    %% SETTERS
    
    %% VALIDATORS
    
    %% EXPORT
    function refs = export(obj, fid, fullpath, refs)
        refs = export@types.core.NWBContainer(obj, fid, fullpath, refs);
        if any(strcmp(refs, fullpath))
            return;
        end
    end
end

end