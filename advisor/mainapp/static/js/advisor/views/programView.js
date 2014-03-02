var advisor = advisor || {};

advisor.ProgramView = Backbone.View.extend({

  template: _.template( $('#program-template').html() ),

  initialize: function() {
    this.listenTo(this.model, 'change', this.render);
  },

  render: function() {
    this.$el.html( this.template( this.model.toJSON() ) );
    return this;
  },

});
