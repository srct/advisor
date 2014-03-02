var advisor = advisor || {};

advisor.Trajectory = Backbone.RelationalModel.extend({
  urlRoot: '/api/trajectories',

  initialize: function() {
    this.fetch()
  },

  relations: [{
    type: Backbone.HasMany,
    key: 'semesters',
    relatedModel: 'advisor.Semester',
    collectionType: 'advisor.SemesterCollection',
    autoFetch: true,
    reverseRelation: {
      key: 'trajectory',
      includeInJSON: 'id'
    }
  }]
});
