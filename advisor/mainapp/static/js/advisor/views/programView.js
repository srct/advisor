var advisor = advisor || {};

advisor.ProgramView = Backbone.View.extend({

  template: _.template( $('#program-template').html() ),

  initialize: function() {
    this.listenTo(this.model, 'change', this.render);
  },

  events: {
    "click .panel-heading": "render_courses"
  },

  render: function() {
    this.$el.attr('id', 'program' + this.model.get('id')).addClass('panel panel-primary program')
      .html(this.template(this.model.toJSON()));
    this.render_courses();
    return this;
  },

  render_courses: function() {
    var that = this;
    this.model.fetchRelated('requirements', {
      success: function(requirements) {
        that.model.get('requirements').forEach(function(requirement) {
          requirement.fetchRelated('courses', {
            success: function() {
              var courseViews = new advisor.CourseCollectionView();
              courseViews.addAll(requirement.get('courses'));
            }
          })
        })
      }
    })
  }

});
