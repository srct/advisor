var advisor = advisor || {};

advisor.SemesterView = Backbone.View.extend({

  template: _.template( $('#semester-template').html() ),

  initialize: function() {
  },

  events: {
    "click .panel-heading": "render"
  },

  render: function() {
    this.$el.addClass('semester panel panel-info').attr('id', 'semester-' + this.model.get('id'))
      .html(this.template(this.model.toJSON()));
    this.render_courses()
    return this;
  },

  render_courses: function() {
    //this.$('.panel-body').html('');
    var that = this;
    console.log(that.model.get('courses'))
    this.model.fetchRelated('courses', {
      success: function() {
        console.log(that.model.get('courses'));
        var courseViews = new advisor.CourseCollectionView({el: that.el});
        courseViews.addAll(that.model.get('courses'));
      },
    });
  }
});
