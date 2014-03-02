var advisor = advisor || {};

advisor.CourseCollectionView = Backbone.View.extend({

  elements: [],

  addOne: function(course) {
    var view = new advisor.CourseView({ model: course });
    // Fix bug where element render multiple times
    var elm = view.render().el
    if(!($('#' + elm.id).length))
      this.$el.append(elm);
  },

  // Add all items in the **Todos** collection at once.
  addAll: function(courses) {
    courses.each(this.addOne, this);
  }

});
