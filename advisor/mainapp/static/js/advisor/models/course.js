var advisor = advisor || {};

advisor.Course = Backbone.RelationalModel.extend({

  defaults: {
    dept: '',
    courseid: 0,
    description: ''
  },

  // Toggle the `completed` state of this todo item.
  toggle: function() {
    this.save({
      completed: !this.get('completed')
    });
  }

});
