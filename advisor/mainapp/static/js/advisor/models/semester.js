var advisor = advisor || {};

advisor.Semester = Backbone.RelationalModel.extend({
  urlRoot: '/api/semesters',

  initialize: function() {
    this.fetchRelated('courses')
  },
  
  events: {
  },

  relations: [{
    type: Backbone.HasMany,
    key: 'courses',
    relatedModel: 'advisor.Course',
    collectionType: 'advisor.CourseCollection',
    reverseRelation: {
      key: 'semester',
      includeInJSON: 'id'
    }
  }],
});
