var advisor = advisor || {};

advisor.Program = Backbone.RelationalModel.extend({
  relations: [{
    type: Backbone.HasMany,
    key: 'requirements',
    relatedModel: 'advisor.Requirement',
    collectionType: 'RequirementCollection',
    reverseRelation: {
      key: 'program',
      includeInJSON: 'id'
    }
  }]
});
