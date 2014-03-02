var advisor = advisor || {};

advisor.SemesterCollectionView = Backbone.View.extend({

  el: '#semesters',

  initialize: function() {
    this.addAll();
  },

  addOne: function(semester) {
    var view = new advisor.SemesterView({ model: semester });
    var el = view.render().el
    $('#semesters').append(el);
  },

  addAll: function() {
    //this.$el.html('');
    advisor.Semesters.each(this.addOne, this);
  },

});
