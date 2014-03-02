var advisor = advisor || {};

advisor.CourseView = Backbone.View.extend({

  tagName: 'div',

  template: _.template( $('#course-template').html() ),

  events: {
    "click": "info"
  },

  initialize: function() {
    this.listenTo(this.model, 'change', this.render);
  },

  // Re-renders the titles of the todo item.
  render: function() {
    $('body').append( this.template( this.model.toJSON() ) );
    return this;
  },

  info: function() {
    
  }
});
