var advisor = advisor || {};

advisor.CourseCollectionView = Backbone.View.extend({

  el: '#program3',
  elements: [],

  addOne: function(course) {
    var view = new advisor.CourseView({ model: course });
    console.log(this.$el);
    this.$el.append(view.render().el);
  },

  // Add all items in the **Todos** collection at once.
  addAll: function(courses) {
    courses.each(this.addOne, this);
  }

});
