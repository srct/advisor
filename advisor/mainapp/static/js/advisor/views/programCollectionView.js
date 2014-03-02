var advisor = advisor || {};

advisor.ProgramCollectionView = Backbone.View.extend({

  el: '#programs',

  initialize: function() {
    this.addAll();
  },

  addOne: function(program) {
    var view = new advisor.ProgramView({ model: program });
    var el = view.render().el
    this.$el.append(el);
  },

  addAll: function() {
    this.$el.html('');
    advisor.Programs.each(this.addOne, this);
  }

});
