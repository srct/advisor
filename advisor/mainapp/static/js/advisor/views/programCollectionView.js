var advisor = advisor || {};

advisor.ProgramCollectionView = Backbone.View.extend({

  el: '#programs',

  initialize: function() {
    this.addAll();
  },

  addOne: function(program) {
    var view = new advisor.ProgramView({ model: program });
    this.$el.append( view.render().el );
  },

  // Add all items in the **Todos** collection at once.
  addAll: function() {
    this.$el.html('');
    advisor.Programs.each(this.addOne, this);
  }

});
