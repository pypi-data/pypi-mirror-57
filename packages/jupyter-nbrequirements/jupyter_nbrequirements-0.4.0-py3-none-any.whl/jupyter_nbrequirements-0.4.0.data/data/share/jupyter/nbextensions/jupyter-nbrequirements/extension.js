define(function() { return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/extension.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/extension.js":
/*!**************************!*\
  !*** ./src/extension.js ***!
  \**************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("/**\n * Jupyter NBRequirements.\n *\n * This file contains the javascript that is run when the notebook is loaded.\n * It contains some requirejs configuration and the `load_ipython_extension`\n * which is required for any notebook extension.\n *\n * @link   https://github.com/CermakM/jupyter-nbrequirements#readme\n * @file   This file loads the Jupyter magic extension for managing notebook requirements.\n * @author Marek Cermak <macermak@redhat.com>\n * @since  0.0.1\n */\n\n/* eslint-disable */\n\nconst __extension__ = \"jupyter_nbrequirements\"\n\n// Some static assets may be required by the custom widget javascript. The base\n// url for the notebook is not known at build time and is therefore computed\n// dynamically.\n__webpack_require__.p = document.querySelector( \"body\" ).getAttribute( 'data-base-url' ) + 'nbextensions/jupyter-nbrequirements/';\n\n/** Constants **/\n// Logging level\nwindow.DEFAULT_LOGGING_LEVEL = { value: 2, name: \"DEBUG\" }\n// Notification timeout in ms\nwindow.DEFAULT_NOTIFICATION_TIMEOUT = 30000\n// Resolution engine {pipenv, thoth}\nwindow.DEFAULT_RESOLUTION_ENGINE = \"pipenv\"\n\n// Load the extension\nif ( window.require ) {\n    window.require.config( {\n        map: {\n            \"*\": {\n                \"nbrequirements\": \"nbextensions/jupyter-nbrequirements/index\"\n            }\n        }\n    } );\n}\n\n// Export the required load_ipython_extension\nmodule.exports = {\n    load_ipython_extension: function () {// Autoload\n        // wait for both the kernel and the jupyter-require extension to be loaded\n        window.require( [\n            \"base/js/namespace\",\n            \"base/js/events\",\n        ], ( Jupyter, events ) => {\n            const options = {\n                silent: false,\n                // if there is an error, let user try to manually\n                // load the extension himself and finish the extension\n                // loading anyway\n                stop_on_error: true,\n                store_history: false\n            }\n\n            // Wait for the required extension to be loaded\n            events.on( \"extension_loaded.JupyterRequire\", () => {\n\n                window.require( [ 'nbrequirements' ], ( module ) => {\n                    Promise.resolve( module.vm )\n                        .then( ( vm ) => window.vm = vm )\n\n                    console.info( \"Loading magic commands: [ '%dep', '%requirements', '%kernel' ]\" )\n\n                    const cmd = \"%reload_ext \" + __extension__\n                    Jupyter.notebook.kernel.execute( cmd, {}, options )\n\n                    console.log( \"Loaded extension: jupyter-nbrequirements\" )\n                } )\n\n            } )\n        } )\n    }\n};\n\n\n//# sourceURL=webpack:///./src/extension.js?");

/***/ })

/******/ })});;