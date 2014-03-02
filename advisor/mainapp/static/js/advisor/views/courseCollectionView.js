var advisor = advisor || {};

advisor.CourseCollectionView = Backbone.View.extend({

  elements: [],

  addOne: function(course) {
    var view = new advisor.CourseView({ model: course });
    // Fix bug where element render multiple times
    var elm = view.render().el
    console.log(elm)
    $('#' + elm.id).remove()
    this.$el.append(elm);
  },

  // Add all items in the **Todos** collection at once.
  addAll: function(courses) {
    courses.each(this.addOne, this);
    (function() {console.log("done")})();
  }

});
