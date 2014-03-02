var advisor = advisor || {};

advisor.Program = Backbone.RelationalModel.extend({
  relations: [{
    type: Backbone.HasMany,
    key: 'requirements',
    relatedModel: 'advisor.Requirements',
    collectionType: 'RequirementCollection',
    reverseRelation: {
      key: 'satisfies',
      includeInJSON: 'id'
    }
  }]
});
