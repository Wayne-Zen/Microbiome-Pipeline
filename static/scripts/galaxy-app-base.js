define(["mvc/user/user-model","utils/metrics-logger","utils/add-logging","utils/localization","bootstrapped-data"],function(a,b,c,d,e){function f(a){var b=this;return b._init(a||{})}return c(f,"GalaxyApp"),f.prototype.defaultOptions={patchExisting:!0,root:"/"},f.prototype._init=function(a){var b=this;return _.extend(b,Backbone.Events),b._processOptions(a),b.debug("GalaxyApp.options: ",b.options),b._patchGalaxy(window.Galaxy),b._initLogger(a.loggerOptions||{}),b.debug("GalaxyApp.logger: ",b.logger),b._initLocale(),b.debug("GalaxyApp.localize: ",b.localize),b.config=a.config||e.config||{},b.debug("GalaxyApp.config: ",b.config),b._initUser(a.user||e.user||{}),b.debug("GalaxyApp.user: ",b.user),b.trigger("ready",b),b._setUpListeners(),b},f.prototype._processOptions=function(a){var b=this,c=b.defaultOptions;b.debug("_processOptions: ",a),b.options={};for(var d in c)c.hasOwnProperty(d)&&(b.options[d]=a.hasOwnProperty(d)?a[d]:c[d]);return b},f.prototype._patchGalaxy=function(a){var b=this;if(b.options.patchExisting&&a){b.debug("found existing Galaxy object:",a);for(var c in a)a.hasOwnProperty(c)&&(b.debug("	 patching in "+c+" to Galaxy"),b[c]=a[c])}},f.prototype._initLogger=function(a){var c=this;return c.debug("_initLogger:",a),c.logger=new b.MetricsLogger(a),c},f.prototype._initLocale=function(a){var b=this;return b.debug("_initLocale:",a),b.localize=d,window._l=b.localize,b},f.prototype._initUser=function(b){var c=this;return c.debug("_initUser:",b),c.user=new a.User(b),c.currUser=c.user,c},f.prototype._setUpListeners=function(){var a=this;return a.lastAjax={},$(document).bind("ajaxSend",function(b,c,d){var e=d.data;try{e=JSON.parse(e)}catch(f){}a.lastAjax={url:location.href.slice(0,-1)+d.url,data:e}}),a._listenToGalaxyMain(),a},f.prototype._listenToGalaxyMain=function(){var a=this,b="iframe#galaxy_main",c=$(b);if(c=c.size()?c.get(0).contentWindow:void 0){var d=function(){try{var c=$(b).get(0).contentWindow,d=c.location.pathname+c.location.search+c.location.hash;a.trigger("galaxy_main:load",{fullpath:d,pathname:c.location.pathname,search:c.location.search,hash:c.location.hash})}catch(e){a.debug("Error handling main frame load:",e)}};$(b).on("load",d)}else a.debug("No galaxy_main found")},f.prototype.toString=function(){var a=this.user.get("email")||"(anonymous)";return"GalaxyApp("+a+")"},{GalaxyApp:f}});
//# sourceMappingURL=../maps/galaxy-app-base.js.map