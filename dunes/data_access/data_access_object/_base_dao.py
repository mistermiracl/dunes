class BaseDao:
    
    def insert(self, obj):
        raise NotImplementedError('Not implemented yet')

    def update(self, obj):
        raise NotImplementedError('Not implemented yet')
    
    def delete(self, identifier):
        raise NotImplementedError('Not implemented yet')

    def find(self, identifier):
        raise NotImplementedError('Not implemented yet')
    
    def find_all(self, identifier=None):
        raise NotImplementedError('Not implemented yet')
        