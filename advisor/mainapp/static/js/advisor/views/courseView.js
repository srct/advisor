var advisor = advisor || {};

advisor.CourseView = Backbone.View.extend({

  template: _.template( $('#course-template').html() ),

  initialize: function() {
    this.listenTo(this.model, 'change', this.render);
  },

  render: function() {
    this.$el.addClass('course ' + this.model.get('dept')).attr('id', 'course-' + this.model.get('id'))
      .html(this.template(this.model.toJSON()));
    return this;
  },
});
