var advisor = advisor || {};

advisor.Course = Backbone.Model.extend({

  defaults: {
    dept: 'CS',
    courseid: 310
    description: "desc"
  },

  // Toggle the `completed` state of this todo item.
  toggle: function() {
    this.save({
      completed: !this.get('completed')
    });
  }

});
