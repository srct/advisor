var advisor = advisor || {};

advisor.Requirement = Backbone.RelationalModel.extend({
  relations: [{
    type: Backbone.HasMany,
    key: 'courses',
    relatedModel: 'advisor.Course',
    collectionType: 'CourseCollection',
    reverseRelation: {
      key: 'satisfies',
      includeInJSON: 'id'
    }
  }]
});
