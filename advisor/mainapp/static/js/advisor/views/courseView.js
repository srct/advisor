var advisor = advisor || {};

advisor.CourseView = Backbone.View.extend({

  template: _.template( $('#course-template').html() ),

  initialize: function() {
    this.listenTo(this.model, 'change', this.render);
  },

  events: {
    "click": "info"
  },

  render: function() {
    this.$el.addClass('course ' + this.model.get('dept')).attr('id', 'course-' + this.model.get('id'))
      .html(this.template(this.model.toJSON()));
    return this;
  },

  info: function() {
    var m = this.model;
    $('#course-info-title').html(m.get('dept') + ' ' + m.get('courseid'));
    $('#course-info-description').text(m.get('description'));
    $('#course-info-prereqs').text(m.get('prerequisites'));
    $("#infoModal").modal();
  }
});
