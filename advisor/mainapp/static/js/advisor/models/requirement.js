var advisor = advisor || {};

advisor.Requirement = Backbone.RelationalModel.extend({
  urlRoot: '/api/requirements',

  defaults: {
    name: '',
  },

  relations: [{
    type: Backbone.HasMany,
    key: 'courses',
    relatedModel: 'advisor.Course',
    collectionType: 'advisor.CourseCollection',
    autoFetch: true,
    reverseRelation: {
      key: 'satisfies',
      includeInJSON: 'id'
    }
  }]
});
