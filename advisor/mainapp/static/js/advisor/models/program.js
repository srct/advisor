var advisor = advisor || {};

advisor.Program = Backbone.RelationalModel.extend({
  urlRoot: '/api/programs',

  initialize: function() {
    this.fetch();
  },

  relations: [{
    type: Backbone.HasMany,
    key: 'requirements',
    relatedModel: 'advisor.Requirement',
    collectionType: 'advisor.RequirementCollection',
    autoFetch: true,
    reverseRelation: {
      key: 'program',
      includeInJSON: 'id'
    }
  }]
});
