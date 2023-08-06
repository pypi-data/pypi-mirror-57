/*! *****************************************************************************
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0

THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
MERCHANTABLITY OR NON-INFRINGEMENT.

See the Apache Version 2.0 License for specific language governing permissions
and limitations under the License.
***************************************************************************** */
function e(e,t,o,r){var i,n=arguments.length,s=n<3?t:null===r?r=Object.getOwnPropertyDescriptor(t,o):r;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)s=Reflect.decorate(e,t,o,r);else for(var a=e.length-1;a>=0;a--)(i=e[a])&&(s=(n<3?i(s):n>3?i(t,o,s):i(t,o))||s);return n>3&&s&&Object.defineProperty(t,o,s),s
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */}const t=new WeakMap,o=e=>"function"==typeof e&&t.has(e),r=void 0!==window.customElements&&void 0!==window.customElements.polyfillWrapFlushCallback,i=(e,t,o=null)=>{for(;t!==o;){const o=t.nextSibling;e.removeChild(t),t=o}},n={},s={},a=`{{lit-${String(Math.random()).slice(2)}}}`,l=`\x3c!--${a}--\x3e`,c=new RegExp(`${a}|${l}`),p="$lit$";class d{constructor(e,t){this.parts=[],this.element=t;const o=[],r=[],i=document.createTreeWalker(t.content,133,null,!1);let n=0,s=-1,l=0;const{strings:d,values:{length:u}}=e;for(;l<u;){const e=i.nextNode();if(null!==e){if(s++,1===e.nodeType){if(e.hasAttributes()){const t=e.attributes,{length:o}=t;let r=0;for(let e=0;e<o;e++)h(t[e].name,p)&&r++;for(;r-- >0;){const t=d[l],o=m.exec(t)[2],r=o.toLowerCase()+p,i=e.getAttribute(r);e.removeAttribute(r);const n=i.split(c);this.parts.push({type:"attribute",index:s,name:o,strings:n}),l+=n.length-1}}"TEMPLATE"===e.tagName&&(r.push(e),i.currentNode=e.content)}else if(3===e.nodeType){const t=e.data;if(t.indexOf(a)>=0){const r=e.parentNode,i=t.split(c),n=i.length-1;for(let t=0;t<n;t++){let o,n=i[t];if(""===n)o=g();else{const e=m.exec(n);null!==e&&h(e[2],p)&&(n=n.slice(0,e.index)+e[1]+e[2].slice(0,-p.length)+e[3]),o=document.createTextNode(n)}r.insertBefore(o,e),this.parts.push({type:"node",index:++s})}""===i[n]?(r.insertBefore(g(),e),o.push(e)):e.data=i[n],l+=n}}else if(8===e.nodeType)if(e.data===a){const t=e.parentNode;null!==e.previousSibling&&s!==n||(s++,t.insertBefore(g(),e)),n=s,this.parts.push({type:"node",index:s}),null===e.nextSibling?e.data="":(o.push(e),s--),l++}else{let t=-1;for(;-1!==(t=e.data.indexOf(a,t+1));)this.parts.push({type:"node",index:-1}),l++}}else i.currentNode=r.pop()}for(const e of o)e.parentNode.removeChild(e)}}const h=(e,t)=>{const o=e.length-t.length;return o>=0&&e.slice(o)===t},u=e=>-1!==e.index,g=()=>document.createComment(""),m=/([ \x09\x0a\x0c\x0d])([^\0-\x1F\x7F-\x9F "'>=/]+)([ \x09\x0a\x0c\x0d]*=[ \x09\x0a\x0c\x0d]*(?:[^ \x09\x0a\x0c\x0d"'`<>=]*|"[^"]*|'[^']*))$/;
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */
class f{constructor(e,t,o){this.__parts=[],this.template=e,this.processor=t,this.options=o}update(e){let t=0;for(const o of this.__parts)void 0!==o&&o.setValue(e[t]),t++;for(const e of this.__parts)void 0!==e&&e.commit()}_clone(){const e=r?this.template.element.content.cloneNode(!0):document.importNode(this.template.element.content,!0),t=[],o=this.template.parts,i=document.createTreeWalker(e,133,null,!1);let n,s=0,a=0,l=i.nextNode();for(;s<o.length;)if(n=o[s],u(n)){for(;a<n.index;)a++,"TEMPLATE"===l.nodeName&&(t.push(l),i.currentNode=l.content),null===(l=i.nextNode())&&(i.currentNode=t.pop(),l=i.nextNode());if("node"===n.type){const e=this.processor.handleTextExpression(this.options);e.insertAfterNode(l.previousSibling),this.__parts.push(e)}else this.__parts.push(...this.processor.handleAttributeExpressions(l,n.name,n.strings,this.options));s++}else this.__parts.push(void 0),s++;return r&&(document.adoptNode(e),customElements.upgrade(e)),e}}
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */const b=` ${a} `;class y{constructor(e,t,o,r){this.strings=e,this.values=t,this.type=o,this.processor=r}getHTML(){const e=this.strings.length-1;let t="",o=!1;for(let r=0;r<e;r++){const e=this.strings[r],i=e.lastIndexOf("\x3c!--");o=(i>-1||o)&&-1===e.indexOf("--\x3e",i+1);const n=m.exec(e);t+=null===n?e+(o?b:l):e.substr(0,n.index)+n[1]+n[2]+p+n[3]+a}return t+=this.strings[e],t}getTemplateElement(){const e=document.createElement("template");return e.innerHTML=this.getHTML(),e}}
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */const v=e=>null===e||!("object"==typeof e||"function"==typeof e),w=e=>Array.isArray(e)||!(!e||!e[Symbol.iterator]);class k{constructor(e,t,o){this.dirty=!0,this.element=e,this.name=t,this.strings=o,this.parts=[];for(let e=0;e<o.length-1;e++)this.parts[e]=this._createPart()}_createPart(){return new x(this)}_getValue(){const e=this.strings,t=e.length-1;let o="";for(let r=0;r<t;r++){o+=e[r];const t=this.parts[r];if(void 0!==t){const e=t.value;if(v(e)||!w(e))o+="string"==typeof e?e:String(e);else for(const t of e)o+="string"==typeof t?t:String(t)}}return o+=e[t],o}commit(){this.dirty&&(this.dirty=!1,this.element.setAttribute(this.name,this._getValue()))}}class x{constructor(e){this.value=void 0,this.committer=e}setValue(e){e===n||v(e)&&e===this.value||(this.value=e,o(e)||(this.committer.dirty=!0))}commit(){for(;o(this.value);){const e=this.value;this.value=n,e(this)}this.value!==n&&this.committer.commit()}}class _{constructor(e){this.value=void 0,this.__pendingValue=void 0,this.options=e}appendInto(e){this.startNode=e.appendChild(g()),this.endNode=e.appendChild(g())}insertAfterNode(e){this.startNode=e,this.endNode=e.nextSibling}appendIntoPart(e){e.__insert(this.startNode=g()),e.__insert(this.endNode=g())}insertAfterPart(e){e.__insert(this.startNode=g()),this.endNode=e.endNode,e.endNode=this.startNode}setValue(e){this.__pendingValue=e}commit(){for(;o(this.__pendingValue);){const e=this.__pendingValue;this.__pendingValue=n,e(this)}const e=this.__pendingValue;e!==n&&(v(e)?e!==this.value&&this.__commitText(e):e instanceof y?this.__commitTemplateResult(e):e instanceof Node?this.__commitNode(e):w(e)?this.__commitIterable(e):e===s?(this.value=s,this.clear()):this.__commitText(e))}__insert(e){this.endNode.parentNode.insertBefore(e,this.endNode)}__commitNode(e){this.value!==e&&(this.clear(),this.__insert(e),this.value=e)}__commitText(e){const t=this.startNode.nextSibling,o="string"==typeof(e=null==e?"":e)?e:String(e);t===this.endNode.previousSibling&&3===t.nodeType?t.data=o:this.__commitNode(document.createTextNode(o)),this.value=e}__commitTemplateResult(e){const t=this.options.templateFactory(e);if(this.value instanceof f&&this.value.template===t)this.value.update(e.values);else{const o=new f(t,e.processor,this.options),r=o._clone();o.update(e.values),this.__commitNode(r),this.value=o}}__commitIterable(e){Array.isArray(this.value)||(this.value=[],this.clear());const t=this.value;let o,r=0;for(const i of e)o=t[r],void 0===o&&(o=new _(this.options),t.push(o),0===r?o.appendIntoPart(this):o.insertAfterPart(t[r-1])),o.setValue(i),o.commit(),r++;r<t.length&&(t.length=r,this.clear(o&&o.endNode))}clear(e=this.startNode){i(this.startNode.parentNode,e.nextSibling,this.endNode)}}class A{constructor(e,t,o){if(this.value=void 0,this.__pendingValue=void 0,2!==o.length||""!==o[0]||""!==o[1])throw new Error("Boolean attributes can only contain a single expression");this.element=e,this.name=t,this.strings=o}setValue(e){this.__pendingValue=e}commit(){for(;o(this.__pendingValue);){const e=this.__pendingValue;this.__pendingValue=n,e(this)}if(this.__pendingValue===n)return;const e=!!this.__pendingValue;this.value!==e&&(e?this.element.setAttribute(this.name,""):this.element.removeAttribute(this.name),this.value=e),this.__pendingValue=n}}class S extends k{constructor(e,t,o){super(e,t,o),this.single=2===o.length&&""===o[0]&&""===o[1]}_createPart(){return new $(this)}_getValue(){return this.single?this.parts[0].value:super._getValue()}commit(){this.dirty&&(this.dirty=!1,this.element[this.name]=this._getValue())}}class $ extends x{}let E=!1;try{const e={get capture(){return E=!0,!1}};window.addEventListener("test",e,e),window.removeEventListener("test",e,e)}catch(e){}class z{constructor(e,t,o){this.value=void 0,this.__pendingValue=void 0,this.element=e,this.eventName=t,this.eventContext=o,this.__boundHandleEvent=e=>this.handleEvent(e)}setValue(e){this.__pendingValue=e}commit(){for(;o(this.__pendingValue);){const e=this.__pendingValue;this.__pendingValue=n,e(this)}if(this.__pendingValue===n)return;const e=this.__pendingValue,t=this.value,r=null==e||null!=t&&(e.capture!==t.capture||e.once!==t.once||e.passive!==t.passive),i=null!=e&&(null==t||r);r&&this.element.removeEventListener(this.eventName,this.__boundHandleEvent,this.__options),i&&(this.__options=C(e),this.element.addEventListener(this.eventName,this.__boundHandleEvent,this.__options)),this.value=e,this.__pendingValue=n}handleEvent(e){"function"==typeof this.value?this.value.call(this.eventContext||this.element,e):this.value.handleEvent(e)}}const C=e=>e&&(E?{capture:e.capture,passive:e.passive,once:e.once}:e.capture);
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */const T=new class{handleAttributeExpressions(e,t,o,r){const i=t[0];if("."===i){return new S(e,t.slice(1),o).parts}return"@"===i?[new z(e,t.slice(1),r.eventContext)]:"?"===i?[new A(e,t.slice(1),o)]:new k(e,t,o).parts}handleTextExpression(e){return new _(e)}};
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */function R(e){let t=N.get(e.type);void 0===t&&(t={stringsArray:new WeakMap,keyString:new Map},N.set(e.type,t));let o=t.stringsArray.get(e.strings);if(void 0!==o)return o;const r=e.strings.join(a);return o=t.keyString.get(r),void 0===o&&(o=new d(e,e.getTemplateElement()),t.keyString.set(r,o)),t.stringsArray.set(e.strings,o),o}const N=new Map,M=new WeakMap;
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */
(window.litHtmlVersions||(window.litHtmlVersions=[])).push("1.1.2");const P=(e,...t)=>new y(e,t,"html",T),L=133;
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */function I(e,t){const{element:{content:o},parts:r}=e,i=document.createTreeWalker(o,L,null,!1);let n=O(r),s=r[n],a=-1,l=0;const c=[];let p=null;for(;i.nextNode();){a++;const e=i.currentNode;for(e.previousSibling===p&&(p=null),t.has(e)&&(c.push(e),null===p&&(p=e)),null!==p&&l++;void 0!==s&&s.index===a;)s.index=null!==p?-1:s.index-l,n=O(r,n),s=r[n]}c.forEach(e=>e.parentNode.removeChild(e))}const B=e=>{let t=11===e.nodeType?0:1;const o=document.createTreeWalker(e,L,null,!1);for(;o.nextNode();)t++;return t},O=(e,t=-1)=>{for(let o=t+1;o<e.length;o++){const t=e[o];if(u(t))return o}return-1};
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */
const D=(e,t)=>`${e}--${t}`;let j=!0;void 0===window.ShadyCSS?j=!1:void 0===window.ShadyCSS.prepareTemplateDom&&(console.warn("Incompatible ShadyCSS version detected. Please update to at least @webcomponents/webcomponentsjs@2.0.2 and @webcomponents/shadycss@1.3.1."),j=!1);const U=e=>t=>{const o=D(t.type,e);let r=N.get(o);void 0===r&&(r={stringsArray:new WeakMap,keyString:new Map},N.set(o,r));let i=r.stringsArray.get(t.strings);if(void 0!==i)return i;const n=t.strings.join(a);if(i=r.keyString.get(n),void 0===i){const o=t.getTemplateElement();j&&window.ShadyCSS.prepareTemplateDom(o,e),i=new d(t,o),r.keyString.set(n,i)}return r.stringsArray.set(t.strings,i),i},V=["html","svg"],H=new Set,q=(e,t,o)=>{H.add(e);const r=o?o.element:document.createElement("template"),i=t.querySelectorAll("style"),{length:n}=i;if(0===n)return void window.ShadyCSS.prepareTemplateStyles(r,e);const s=document.createElement("style");for(let e=0;e<n;e++){const t=i[e];t.parentNode.removeChild(t),s.textContent+=t.textContent}(e=>{V.forEach(t=>{const o=N.get(D(t,e));void 0!==o&&o.keyString.forEach(e=>{const{element:{content:t}}=e,o=new Set;Array.from(t.querySelectorAll("style")).forEach(e=>{o.add(e)}),I(e,o)})})})(e);const a=r.content;o?function(e,t,o=null){const{element:{content:r},parts:i}=e;if(null==o)return void r.appendChild(t);const n=document.createTreeWalker(r,L,null,!1);let s=O(i),a=0,l=-1;for(;n.nextNode();){for(l++,n.currentNode===o&&(a=B(t),o.parentNode.insertBefore(t,o));-1!==s&&i[s].index===l;){if(a>0){for(;-1!==s;)i[s].index+=a,s=O(i,s);return}s=O(i,s)}}}(o,s,a.firstChild):a.insertBefore(s,a.firstChild),window.ShadyCSS.prepareTemplateStyles(r,e);const l=a.querySelector("style");if(window.ShadyCSS.nativeShadow&&null!==l)t.insertBefore(l.cloneNode(!0),t.firstChild);else if(o){a.insertBefore(s,a.firstChild);const e=new Set;e.add(s),I(o,e)}};window.JSCompiler_renameProperty=(e,t)=>e;const F={toAttribute(e,t){switch(t){case Boolean:return e?"":null;case Object:case Array:return null==e?e:JSON.stringify(e)}return e},fromAttribute(e,t){switch(t){case Boolean:return null!==e;case Number:return null===e?null:Number(e);case Object:case Array:return JSON.parse(e)}return e}},G=(e,t)=>t!==e&&(t==t||e==e),Z={attribute:!0,type:String,converter:F,reflect:!1,hasChanged:G},Y=Promise.resolve(!0),W=1,Q=4,K=8,X=16,J=32,ee="finalized";class te extends HTMLElement{constructor(){super(),this._updateState=0,this._instanceProperties=void 0,this._updatePromise=Y,this._hasConnectedResolver=void 0,this._changedProperties=new Map,this._reflectingProperties=void 0,this.initialize()}static get observedAttributes(){this.finalize();const e=[];return this._classProperties.forEach((t,o)=>{const r=this._attributeNameForProperty(o,t);void 0!==r&&(this._attributeToPropertyMap.set(r,o),e.push(r))}),e}static _ensureClassProperties(){if(!this.hasOwnProperty(JSCompiler_renameProperty("_classProperties",this))){this._classProperties=new Map;const e=Object.getPrototypeOf(this)._classProperties;void 0!==e&&e.forEach((e,t)=>this._classProperties.set(t,e))}}static createProperty(e,t=Z){if(this._ensureClassProperties(),this._classProperties.set(e,t),t.noAccessor||this.prototype.hasOwnProperty(e))return;const o="symbol"==typeof e?Symbol():`__${e}`;Object.defineProperty(this.prototype,e,{get(){return this[o]},set(t){const r=this[e];this[o]=t,this._requestUpdate(e,r)},configurable:!0,enumerable:!0})}static finalize(){const e=Object.getPrototypeOf(this);if(e.hasOwnProperty(ee)||e.finalize(),this[ee]=!0,this._ensureClassProperties(),this._attributeToPropertyMap=new Map,this.hasOwnProperty(JSCompiler_renameProperty("properties",this))){const e=this.properties,t=[...Object.getOwnPropertyNames(e),..."function"==typeof Object.getOwnPropertySymbols?Object.getOwnPropertySymbols(e):[]];for(const o of t)this.createProperty(o,e[o])}}static _attributeNameForProperty(e,t){const o=t.attribute;return!1===o?void 0:"string"==typeof o?o:"string"==typeof e?e.toLowerCase():void 0}static _valueHasChanged(e,t,o=G){return o(e,t)}static _propertyValueFromAttribute(e,t){const o=t.type,r=t.converter||F,i="function"==typeof r?r:r.fromAttribute;return i?i(e,o):e}static _propertyValueToAttribute(e,t){if(void 0===t.reflect)return;const o=t.type,r=t.converter;return(r&&r.toAttribute||F.toAttribute)(e,o)}initialize(){this._saveInstanceProperties(),this._requestUpdate()}_saveInstanceProperties(){this.constructor._classProperties.forEach((e,t)=>{if(this.hasOwnProperty(t)){const e=this[t];delete this[t],this._instanceProperties||(this._instanceProperties=new Map),this._instanceProperties.set(t,e)}})}_applyInstanceProperties(){this._instanceProperties.forEach((e,t)=>this[t]=e),this._instanceProperties=void 0}connectedCallback(){this._updateState=this._updateState|J,this._hasConnectedResolver&&(this._hasConnectedResolver(),this._hasConnectedResolver=void 0)}disconnectedCallback(){}attributeChangedCallback(e,t,o){t!==o&&this._attributeToProperty(e,o)}_propertyToAttribute(e,t,o=Z){const r=this.constructor,i=r._attributeNameForProperty(e,o);if(void 0!==i){const e=r._propertyValueToAttribute(t,o);if(void 0===e)return;this._updateState=this._updateState|K,null==e?this.removeAttribute(i):this.setAttribute(i,e),this._updateState=this._updateState&~K}}_attributeToProperty(e,t){if(this._updateState&K)return;const o=this.constructor,r=o._attributeToPropertyMap.get(e);if(void 0!==r){const e=o._classProperties.get(r)||Z;this._updateState=this._updateState|X,this[r]=o._propertyValueFromAttribute(t,e),this._updateState=this._updateState&~X}}_requestUpdate(e,t){let o=!0;if(void 0!==e){const r=this.constructor,i=r._classProperties.get(e)||Z;r._valueHasChanged(this[e],t,i.hasChanged)?(this._changedProperties.has(e)||this._changedProperties.set(e,t),!0!==i.reflect||this._updateState&X||(void 0===this._reflectingProperties&&(this._reflectingProperties=new Map),this._reflectingProperties.set(e,i))):o=!1}!this._hasRequestedUpdate&&o&&this._enqueueUpdate()}requestUpdate(e,t){return this._requestUpdate(e,t),this.updateComplete}async _enqueueUpdate(){let e,t;this._updateState=this._updateState|Q;const o=this._updatePromise;this._updatePromise=new Promise((o,r)=>{e=o,t=r});try{await o}catch(e){}this._hasConnected||await new Promise(e=>this._hasConnectedResolver=e);try{const e=this.performUpdate();null!=e&&await e}catch(e){t(e)}e(!this._hasRequestedUpdate)}get _hasConnected(){return this._updateState&J}get _hasRequestedUpdate(){return this._updateState&Q}get hasUpdated(){return this._updateState&W}performUpdate(){this._instanceProperties&&this._applyInstanceProperties();let e=!1;const t=this._changedProperties;try{e=this.shouldUpdate(t),e&&this.update(t)}catch(t){throw e=!1,t}finally{this._markUpdated()}e&&(this._updateState&W||(this._updateState=this._updateState|W,this.firstUpdated(t)),this.updated(t))}_markUpdated(){this._changedProperties=new Map,this._updateState=this._updateState&~Q}get updateComplete(){return this._getUpdateComplete()}_getUpdateComplete(){return this._updatePromise}shouldUpdate(e){return!0}update(e){void 0!==this._reflectingProperties&&this._reflectingProperties.size>0&&(this._reflectingProperties.forEach((e,t)=>this._propertyToAttribute(t,this[t],e)),this._reflectingProperties=void 0)}updated(e){}firstUpdated(e){}}te[ee]=!0;
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */
const oe=e=>t=>"function"==typeof t?((e,t)=>(window.customElements.define(e,t),t))(e,t):((e,t)=>{const{kind:o,elements:r}=t;return{kind:o,elements:r,finisher(t){window.customElements.define(e,t)}}})(e,t),re=(e,t)=>"method"!==t.kind||!t.descriptor||"value"in t.descriptor?{kind:"field",key:Symbol(),placement:"own",descriptor:{},initializer(){"function"==typeof t.initializer&&(this[t.key]=t.initializer.call(this))},finisher(o){o.createProperty(t.key,e)}}:Object.assign({},t,{finisher(o){o.createProperty(t.key,e)}}),ie=(e,t,o)=>{t.constructor.createProperty(o,e)};function ne(e){return(t,o)=>void 0!==o?ie(e,t,o):re(e,t)}
/**
@license
Copyright (c) 2019 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at
http://polymer.github.io/LICENSE.txt The complete set of authors may be found at
http://polymer.github.io/AUTHORS.txt The complete set of contributors may be
found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by Google as
part of the polymer project is also subject to an additional IP rights grant
found at http://polymer.github.io/PATENTS.txt
*/const se="adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,ae=Symbol();class le{constructor(e,t){if(t!==ae)throw new Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e}get styleSheet(){return void 0===this._styleSheet&&(se?(this._styleSheet=new CSSStyleSheet,this._styleSheet.replaceSync(this.cssText)):this._styleSheet=null),this._styleSheet}toString(){return this.cssText}}const ce=(e,...t)=>{const o=t.reduce((t,o,r)=>t+(e=>{if(e instanceof le)return e.cssText;if("number"==typeof e)return e;throw new Error(`Value passed to 'css' function must be a 'css' function result: ${e}. Use 'unsafeCSS' to pass non-literal values, but\n            take care to ensure page security.`)})(o)+e[r+1],e[0]);return new le(o,ae)};
/**
 * @license
 * Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */
(window.litElementVersions||(window.litElementVersions=[])).push("2.2.1");const pe=e=>e.flat?e.flat(1/0):function e(t,o=[]){for(let r=0,i=t.length;r<i;r++){const i=t[r];Array.isArray(i)?e(i,o):o.push(i)}return o}(e);class de extends te{static finalize(){super.finalize.call(this),this._styles=this.hasOwnProperty(JSCompiler_renameProperty("styles",this))?this._getUniqueStyles():this._styles||[]}static _getUniqueStyles(){const e=this.styles,t=[];if(Array.isArray(e)){pe(e).reduceRight((e,t)=>(e.add(t),e),new Set).forEach(e=>t.unshift(e))}else e&&t.push(e);return t}initialize(){super.initialize(),this.renderRoot=this.createRenderRoot(),window.ShadowRoot&&this.renderRoot instanceof window.ShadowRoot&&this.adoptStyles()}createRenderRoot(){return this.attachShadow({mode:"open"})}adoptStyles(){const e=this.constructor._styles;0!==e.length&&(void 0===window.ShadyCSS||window.ShadyCSS.nativeShadow?se?this.renderRoot.adoptedStyleSheets=e.map(e=>e.styleSheet):this._needsShimAdoptedStyleSheets=!0:window.ShadyCSS.ScopingShim.prepareAdoptedCssText(e.map(e=>e.cssText),this.localName))}connectedCallback(){super.connectedCallback(),this.hasUpdated&&void 0!==window.ShadyCSS&&window.ShadyCSS.styleElement(this)}update(e){super.update(e);const t=this.render();t instanceof y&&this.constructor.render(t,this.renderRoot,{scopeName:this.localName,eventContext:this}),this._needsShimAdoptedStyleSheets&&(this._needsShimAdoptedStyleSheets=!1,this.constructor._styles.forEach(e=>{const t=document.createElement("style");t.textContent=e.cssText,this.renderRoot.appendChild(t)}))}render(){}}function he(){if(customElements.get("hui-view"))return!0;const e=document.createElement("partial-panel-resolver");e.hass=document.querySelector("home-assistant").hass,e.route={path:"/lovelace/"};try{document.querySelector("home-assistant").appendChild(e).catch(e=>{})}catch(t){document.querySelector("home-assistant").removeChild(e)}return!!customElements.get("hui-view")}de.finalized=!0,de.render=(e,t,o)=>{if(!o||"object"!=typeof o||!o.scopeName)throw new Error("The `scopeName` option is required.");const r=o.scopeName,n=M.has(t),s=j&&11===t.nodeType&&!!t.host,a=s&&!H.has(r),l=a?document.createDocumentFragment():t;if(((e,t,o)=>{let r=M.get(t);void 0===r&&(i(t,t.firstChild),M.set(t,r=new _(Object.assign({templateFactory:R},o))),r.appendInto(t)),r.setValue(e),r.commit()})(e,l,Object.assign({templateFactory:U(r)},o)),a){const e=M.get(l);M.delete(l);const o=e.value instanceof f?e.value.template:void 0;q(r,l,o),i(t,t.firstChild),t.appendChild(l),M.set(t,e)}!n&&s&&window.ShadyCSS.styleElement(t.host)};const ue=(e,t)=>{history.pushState(null,"",t)};const ge=[ce`
    :host {
      @apply --paper-font-body1;
    }

    app-header-layout,
    ha-app-layout {
      background-color: var(--primary-background-color);
    }

    app-header, app-toolbar {
      background-color: var(--primary-color);
      font-weight: 400;
      color: var(--text-primary-color, white);
    }

    app-toolbar ha-menu-button + [main-title],
    app-toolbar ha-paper-icon-button-arrow-prev + [main-title],
    app-toolbar paper-icon-button + [main-title] {
      margin-left: 24px;
    }

    button.link {
      background: none;
      color: inherit;
      border: none;
      padding: 0;
      font: inherit;
      text-align: left;
      text-decoration: underline;
      cursor: pointer;
    }

    .card-actions a {
      text-decoration: none;
    }

    .card-actions .warning {
      --mdc-theme-primary: var(--google-red-500);
    }
`,ce`
    :host {
      font-family: var(--paper-font-body1_-_font-family);
      -webkit-font-smoothing: var(--paper-font-body1_-_-webkit-font-smoothing);
      font-size: var(--paper-font-body1_-_font-size);
      font-weight: var(--paper-font-body1_-_font-weight);
      line-height: var(--paper-font-body1_-_line-height);
    }

    app-header-layout, ha-app-layout {
      background-color: var(--primary-background-color);
    }

    app-header, app-toolbar, paper-tabs {
      background-color: var(--primary-color);
      font-weight: 400;
      text-transform: uppercase;
      color: var(--text-primary-color, white);
    }

    paper-tabs {
      --paper-tabs-selection-bar-color: #fff;
      margin-left: 12px;
    }

    app-toolbar ha-menu-button + [main-title], app-toolbar ha-paper-icon-button-arrow-prev + [main-title], app-toolbar paper-icon-button + [main-title] {
      margin-left: 24px;
    }
`,ce`
    :root {
        font-family: var(--paper-font-body1_-_font-family);
        -webkit-font-smoothing: var(--paper-font-body1_-_-webkit-font-smoothing);
        font-size: var(--paper-font-body1_-_font-size);
        font-weight: var(--paper-font-body1_-_font-weight);
        line-height: var(--paper-font-body1_-_line-height);
    }
    :host {
        --hacs-status-installed: #126e15;
        --hacs-status-pending-update: #ffab40;
        --hacs-status-pending-restart: var(--google-red-500);
        --hacs-status-not-loaded: var(--google-red-500);
        --hacs-badge-color: var(--primary-color);
    }
    a {
        text-decoration: none;
        color: var(--dark-primary-color);
    }
    h1 {
        font-family: var(--paper-font-title_-_font-family);
        -webkit-font-smoothing: var(--paper-font-title_-_-webkit-font-smoothing);
        white-space: var(--paper-font-title_-_white-space);
        overflow: var(--paper-font-title_-_overflow);
        text-overflow: var(--paper-font-title_-_text-overflow);
        font-size: var(--paper-font-title_-_font-size);
        font-weight: var(--paper-font-title_-_font-weight);
        line-height: var(--paper-font-title_-_line-height);
        @apply --paper-font-title;
    }
    .title {
        margin-bottom: 16px;
        padding-top: 4px;
        color: var(--primary-text-color);
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
    }
    .addition {
        color: var(--secondary-text-color);
        position: relative;
        height: auto;
        line-height: 1.2em;
        text-overflow: ellipsis;
        overflow: hidden;
    }
    paper-card {
        cursor: pointer;
    }
    ha-card {
      margin: 8px;
    }
    ha-icon {
        height: 24px;
        width: 24px;
        margin-right: 16px;
        float: left;
        color: var(--primary-text-color);
    }
    ha-icon.installed {
        color: var(--hacs-status-installed);
    }
    ha-icon.pending-upgrade {
        color: var(--hacs-status-pending-update);
    }
    ha-icon.pending-restart {
        color: var(--hacs-status-pending-restart);
    }
    ha-icon.not-loaded {
        color: var(--hacs-status-not-loaded);
    }
    ha-icon.new {
        color: var(--hacs-badge-color);
      }
`,ce`
    @media screen and (max-width: 600px) and (min-width: 0) {
      .MobileHide {
          display: none !important;
      }
      .MobileGrid {
          display: grid !important;
          text-align: center !important;
          position: initial !important;
          width: 100% !important;
          padding-left: 0px !important;
          padding-right: 0px !important;
      }
      hacs-help-button {
          display: none;
      }
    }
`];let me=class extends de{render(){return P`
        <a href="#">
            <ha-icon
                title="Documentation"
                class="float"
                icon="mdi:help"
                @click=${this.openHelp}>
            </ha-icon>
        </a>
        `}openHelp(){var e=window.location.pathname.split("/")[2];"integration"===e&&(e="stores"),"plugin"===e&&(e="stores"),"appdaemon"===e&&(e="stores"),"python_script"===e&&(e="stores"),"theme"===e&&(e="stores"),window.open(`https://hacs.xyz/docs/navigation/${e}`,"Help","noreferrer")}static get styles(){return[ge,ce`
            .float{
                position: fixed;
                width: 36px;
                height:36px;
                bottom: 24px;
                right: 24px;
                border-radius: 50px;
                border: 4px solid var(--accent-color);
                text-align: center;
                color: var(--paper-card-background-color, var(--primary-background-color));
                background-color: var(--accent-color);
            }
        `]}};function fe(e,t,o){if("yaml"===o.lovelace_mode)return!0;if(void 0!==t){var r=!1,i=`/community_plugin/${e.full_name.split("/")[1]}/${e.file_name}`;return void 0!==t.resources&&t.resources.forEach(e=>{r||e.url===i&&(r=!0)}),r}return!0}me=e([oe("hacs-help-button")],me);class be extends de{static get styles(){return ge}}e([ne()],be.prototype,"hass",void 0),e([ne()],be.prototype,"repository",void 0),e([ne()],be.prototype,"status",void 0);let ye=class extends be{render(){return P`
            <mwc-button @click=${this.ExecuteAction}>
                ${this.hass.localize("component.hacs.store.clear_new")}
            </mwc-button>
        `}ExecuteAction(){var e={type:"hacs/settings",action:"clear_new",category:this.category};this.hass.connection.sendMessage(e)}};e([ne()],ye.prototype,"category",void 0),ye=e([oe("hacs-button-clear-new")],ye);let ve=class extends de{constructor(){super(...arguments),this.repository_view=!1,this.SortKey="name",this.SearchTerm=""}render(){if("repository"===this.panel)return P`
      <hacs-panel-repository
        .hass=${this.hass}
        .route=${this.route}
        .status=${this.status}
        .configuration=${this.configuration}
        .repositories=${this.repositories}
        .repository=${this.repository}
        .lovelaceconfig=${this.lovelaceconfig}
      >
      </hacs-panel-repository>`;{const r=this.panel;var e=[];const i=this.configuration;this.SearchTerm=localStorage.getItem("hacs-search");var t=this.SearchTerm,o=this.repositories.filter((function(o){if("installed"!==r){if("172733314"===o.id)return!1;if(o.hide)return!1;if("ALL"!==i.country&&void 0!==o.country&&i.country!==o.country)return!1}else if(o.installed)return!0;return o.category===r&&(""!==t?!!o.name.toLowerCase().includes(t)||(!!o.description.toLowerCase().includes(t)||(!!o.full_name.toLowerCase().includes(t)||(!!String(o.authors).toLowerCase().includes(t)||!!String(o.topics).toLowerCase().includes(t)))):(o.new&&e.push(o),!0))}));return P`
      <div class="store-top store-top-${this.panel}">
        <paper-input
          class="search-bar"
          type="text"
          id="Search"
          @input=${this.DoSearch}
          placeholder="  ${this.hass.localize("component.hacs.store.placeholder_search")}."
          autofocus
          .value=${this.SearchTerm}
        >
          ${this.SearchTerm.length>0?P`
            <ha-icon slot="suffix" icon="mdi:close" @click="${this.clearSearch}"></ha-icon>
          `:""}
        </paper-input>
        <paper-dropdown-menu @value-changed="${this.SetSortKey}" class="sort" label="Sort">
          <paper-listbox slot="dropdown-content" selected="0">
            <paper-item>Name</paper-item>
            <paper-item>Status</paper-item>
          </paper-listbox>
        </paper-dropdown-menu>
        </div>

    ${0!==e.length?P`
    <div class="card-group">
      <h1>${this.hass.localize("component.hacs.store.new_repositories")}</h1>
      ${e.sort((e,t)=>this.SortRepo(e,t)?1:-1).map(e=>P`
          ${"Table"!==this.configuration.frontend_mode?P`
          <paper-card @click="${this.ShowRepository}" .RepoID="${e.id}"
            class="${this.configuration.frontend_compact?"compact":""}">
          <div class="card-content">
            <div>
              <ha-icon
                icon="mdi:new-box"
                class="${this.StatusAndDescription(e).status}"
                title="${this.StatusAndDescription(e).description}"
                >
              </ha-icon>
              <div>
                <div class="title">${e.name}</div>
                <div class="addition">${e.description}</div>
              </div>
            </div>
          </div>
          </paper-card>

        `:P`

        <paper-item .RepoID=${e.id} @click="${this.ShowRepository}"
          class="${this.configuration.frontend_compact?"compact":""}">
          <div class="icon">
            <ha-icon
              icon="mdi:new-box"
              class="${this.StatusAndDescription(e).status}"
              title="${this.StatusAndDescription(e).description}"
          </ha-icon>
          </div>
          <paper-item-body two-line>
            <div>${e.name}</div>
            <div class="addition">${e.description}</div>
          </paper-item-body>
        </paper-item>
        `}
      `)}
    </div>
    <div class="card-group">
      <hacs-button-clear-new .hass=${this.hass} .category=${r}></hacs-button-clear-new>
    </div>
    <hr>
    `:""}

    <div class="card-group">
    ${o.sort((e,t)=>this.SortRepo(e,t)?1:-1).map(e=>P`

      ${"Table"!==this.configuration.frontend_mode?P`
        <paper-card @click="${this.ShowRepository}" .RepoID="${e.id}"
          class="${this.configuration.frontend_compact?"compact":""}">
        <div class="card-content">
          <div>
            <ha-icon
              icon=${e.new?"mdi:new-box":"mdi:cube"}
              class="${this.StatusAndDescription(e).status}"
              title="${this.StatusAndDescription(e).description}"
              >
            </ha-icon>
            <div>
              <div class="title">${e.name}</div>
              <div class="addition">${e.description}</div>
            </div>
          </div>
        </div>
        </paper-card>

      `:P`

      <paper-item .RepoID=${e.id} @click="${this.ShowRepository}"
        class="${this.configuration.frontend_compact?"compact":""}">
        <div class="icon">
          <ha-icon
            icon=${e.new?"mdi:new-box":"mdi:cube"}
            class="${this.StatusAndDescription(e).status}"
            title="${this.StatusAndDescription(e).description}"
        </ha-icon>
        </div>
        <paper-item-body two-line>
          <div>${e.name}</div>
          <div class="addition">${e.description}</div>
        </paper-item-body>
      </paper-item>
      `}


      `)}
    </div>`}}SortRepo(e,t){return"stars"===this.SortKey?e.stars<t.stars:"status"===this.SortKey?e.status<t.status:e[this.SortKey]>t[this.SortKey]}SetSortKey(e){0!==e.detail.value.length&&(this.SortKey=e.detail.value.replace(" ","_").toLowerCase())}StatusAndDescription(e){var t=e.status,o=e.status_description;return e.installed&&!this.status.background_task&&("plugin"!==e.category||fe(e,this.lovelaceconfig,this.status)||(t="not-loaded",o="Not loaded in lovelace")),{status:t,description:o}}DoSearch(e){this.SearchTerm=e.composedPath()[0].value.toLowerCase(),localStorage.setItem("hacs-search",this.SearchTerm)}clearSearch(){this.SearchTerm="",localStorage.setItem("hacs-search",this.SearchTerm)}ShowRepository(e){var t;e.composedPath().forEach(e=>{e.RepoID&&(t=e.RepoID)}),this.panel="repository",this.repository=t,this.repository_view=!0,this.requestUpdate(),ue(0,`/${this._rootPath}/repository/${t}`)}get _rootPath(){return"hacs_dev"===window.location.pathname.split("/")[1]?"hacs_dev":"hacs"}static get styles(){return[ge,ce`
      hr {
        width: 95%
      }
      paper-item.list {
        margin-bottom: 24px;
      }
      paper-item:hover {
        outline: 0;
        background: var(--table-row-alternative-background-color);
    }
      .search-bar {
        display: block;
        width: 60%;
        margin-left: 3.4%;
        margin-top: 2%;
        background-color: var(--primary-background-color);
        color: var(--primary-text-color);
        line-height: 32px;
        border-color: var(--dark-primary-color);
        border-width: inherit;
        border-bottom-width: thin;
      }

      .sort {
        display: block;
        width: 30%;
        margin-left: 3.4%;
        margin-top: 2%;
        background-color: var(--primary-background-color);
        color: var(--primary-text-color);
        line-height: 32px;
        border-color: var(--dark-primary-color);
        border-width: inherit;
        border-bottom-width: thin;
      }

      .store-top {
        display: flex;
      }

      .store-top-installed, .store-top-settings {
        display: none;
      }

      paper-card.compact {
        height: 80px !important;
        white-space: nowrap !important;
      }

      paper-item.compact {
        margin-bottom: 2px !important;
        white-space: nowrap !important;
      }

      .card-group {
          margin-top: 24px;
          width: 95%;
          margin-left: 2.5%;
        }

        .card-group .title {
          color: var(--primary-text-color);
          margin-bottom: 12px;
        }

        .card-group .description {
          font-size: 0.5em;
          font-weight: 500;
          margin-top: 4px;
        }

        .card-group paper-card {
          --card-group-columns: 5;
          width: calc((100% - 12px * var(--card-group-columns)) / var(--card-group-columns));
          margin: 4px;
          vertical-align: top;
          height: 136px;
        }

        @media screen and (max-width: 2400px) and (min-width: 1801px) {
          .card-group paper-card {
            --card-group-columns: 4;
          }
        }

        @media screen and (max-width: 1800px) and (min-width: 1201px) {
          .card-group paper-card {
            --card-group-columns: 3;
          }
        }

        @media screen and (max-width: 1200px) and (min-width: 601px) {
          .card-group paper-card {
            --card-group-columns: 2;
          }
        }

        @media screen and (max-width: 600px) and (min-width: 0) {
          .card-group paper-card {
            width: 100%;
            margin: 4px 0;
          }
          .content {
            padding: 0;
          }
        }
    `]}};function we(e,t,o,r){let i;i=void 0!==r?{type:"hacs/repository/data",action:o,repository:t,data:r}:{type:"hacs/repository",action:o,repository:t},e.connection.sendMessage(i)}function ke(e,t){return e(t={exports:{}},t.exports),t.exports}e([ne()],ve.prototype,"hass",void 0),e([ne()],ve.prototype,"repositories",void 0),e([ne()],ve.prototype,"configuration",void 0),e([ne()],ve.prototype,"route",void 0),e([ne()],ve.prototype,"panel",void 0),e([ne()],ve.prototype,"status",void 0),e([ne()],ve.prototype,"repository_view",void 0),e([ne()],ve.prototype,"repository",void 0),e([ne()],ve.prototype,"SortKey",void 0),e([ne()],ve.prototype,"SearchTerm",void 0),e([ne()],ve.prototype,"lovelaceconfig",void 0),ve=e([oe("hacs-panel")],ve);var xe=ke((function(e,t){!function(t){var o={newline:/^\n+/,code:/^( {4}[^\n]+\n*)+/,fences:/^ {0,3}(`{3,}|~{3,})([^`~\n]*)\n(?:|([\s\S]*?)\n)(?: {0,3}\1[~`]* *(?:\n+|$)|$)/,hr:/^ {0,3}((?:- *){3,}|(?:_ *){3,}|(?:\* *){3,})(?:\n+|$)/,heading:/^ {0,3}(#{1,6}) +([^\n]*?)(?: +#+)? *(?:\n+|$)/,blockquote:/^( {0,3}> ?(paragraph|[^\n]*)(?:\n|$))+/,list:/^( {0,3})(bull) [\s\S]+?(?:hr|def|\n{2,}(?! )(?!\1bull )\n*|\s*$)/,html:"^ {0,3}(?:<(script|pre|style)[\\s>][\\s\\S]*?(?:</\\1>[^\\n]*\\n+|$)|comment[^\\n]*(\\n+|$)|<\\?[\\s\\S]*?\\?>\\n*|<![A-Z][\\s\\S]*?>\\n*|<!\\[CDATA\\[[\\s\\S]*?\\]\\]>\\n*|</?(tag)(?: +|\\n|/?>)[\\s\\S]*?(?:\\n{2,}|$)|<(?!script|pre|style)([a-z][\\w-]*)(?:attribute)*? */?>(?=[ \\t]*(?:\\n|$))[\\s\\S]*?(?:\\n{2,}|$)|</(?!script|pre|style)[a-z][\\w-]*\\s*>(?=[ \\t]*(?:\\n|$))[\\s\\S]*?(?:\\n{2,}|$))",def:/^ {0,3}\[(label)\]: *\n? *<?([^\s>]+)>?(?:(?: +\n? *| *\n *)(title))? *(?:\n+|$)/,nptable:f,table:f,lheading:/^([^\n]+)\n {0,3}(=+|-+) *(?:\n+|$)/,_paragraph:/^([^\n]+(?:\n(?!hr|heading|lheading|blockquote|fences|list|html)[^\n]+)*)/,text:/^[^\n]+/};function r(e){this.tokens=[],this.tokens.links=Object.create(null),this.options=e||x.defaults,this.rules=o.normal,this.options.pedantic?this.rules=o.pedantic:this.options.gfm&&(this.rules=o.gfm)}o._label=/(?!\s*\])(?:\\[\[\]]|[^\[\]])+/,o._title=/(?:"(?:\\"?|[^"\\])*"|'[^'\n]*(?:\n[^'\n]+)*\n?'|\([^()]*\))/,o.def=h(o.def).replace("label",o._label).replace("title",o._title).getRegex(),o.bullet=/(?:[*+-]|\d{1,9}\.)/,o.item=/^( *)(bull) ?[^\n]*(?:\n(?!\1bull ?)[^\n]*)*/,o.item=h(o.item,"gm").replace(/bull/g,o.bullet).getRegex(),o.list=h(o.list).replace(/bull/g,o.bullet).replace("hr","\\n+(?=\\1?(?:(?:- *){3,}|(?:_ *){3,}|(?:\\* *){3,})(?:\\n+|$))").replace("def","\\n+(?="+o.def.source+")").getRegex(),o._tag="address|article|aside|base|basefont|blockquote|body|caption|center|col|colgroup|dd|details|dialog|dir|div|dl|dt|fieldset|figcaption|figure|footer|form|frame|frameset|h[1-6]|head|header|hr|html|iframe|legend|li|link|main|menu|menuitem|meta|nav|noframes|ol|optgroup|option|p|param|section|source|summary|table|tbody|td|tfoot|th|thead|title|tr|track|ul",o._comment=/<!--(?!-?>)[\s\S]*?-->/,o.html=h(o.html,"i").replace("comment",o._comment).replace("tag",o._tag).replace("attribute",/ +[a-zA-Z:_][\w.:-]*(?: *= *"[^"\n]*"| *= *'[^'\n]*'| *= *[^\s"'=<>`]+)?/).getRegex(),o.paragraph=h(o._paragraph).replace("hr",o.hr).replace("heading"," {0,3}#{1,6} +").replace("|lheading","").replace("blockquote"," {0,3}>").replace("fences"," {0,3}(?:`{3,}|~{3,})[^`\\n]*\\n").replace("list"," {0,3}(?:[*+-]|1[.)]) ").replace("html","</?(?:tag)(?: +|\\n|/?>)|<(?:script|pre|style|!--)").replace("tag",o._tag).getRegex(),o.blockquote=h(o.blockquote).replace("paragraph",o.paragraph).getRegex(),o.normal=b({},o),o.gfm=b({},o.normal,{nptable:/^ *([^|\n ].*\|.*)\n *([-:]+ *\|[-| :]*)(?:\n((?:.*[^>\n ].*(?:\n|$))*)\n*|$)/,table:/^ *\|(.+)\n *\|?( *[-:]+[-| :]*)(?:\n((?: *[^>\n ].*(?:\n|$))*)\n*|$)/}),o.pedantic=b({},o.normal,{html:h("^ *(?:comment *(?:\\n|\\s*$)|<(tag)[\\s\\S]+?</\\1> *(?:\\n{2,}|\\s*$)|<tag(?:\"[^\"]*\"|'[^']*'|\\s[^'\"/>\\s]*)*?/?> *(?:\\n{2,}|\\s*$))").replace("comment",o._comment).replace(/tag/g,"(?!(?:a|em|strong|small|s|cite|q|dfn|abbr|data|time|code|var|samp|kbd|sub|sup|i|b|u|mark|ruby|rt|rp|bdi|bdo|span|br|wbr|ins|del|img)\\b)\\w+(?!:|[^\\w\\s@]*@)\\b").getRegex(),def:/^ *\[([^\]]+)\]: *<?([^\s>]+)>?(?: +(["(][^\n]+[")]))? *(?:\n+|$)/,heading:/^ *(#{1,6}) *([^\n]+?) *(?:#+ *)?(?:\n+|$)/,fences:f,paragraph:h(o.normal._paragraph).replace("hr",o.hr).replace("heading"," *#{1,6} *[^\n]").replace("lheading",o.lheading).replace("blockquote"," {0,3}>").replace("|fences","").replace("|list","").replace("|html","").getRegex()}),r.rules=o,r.lex=function(e,t){return new r(t).lex(e)},r.prototype.lex=function(e){return e=e.replace(/\r\n|\r/g,"\n").replace(/\t/g,"    ").replace(/\u00a0/g," ").replace(/\u2424/g,"\n"),this.token(e,!0)},r.prototype.token=function(e,t){var r,i,n,s,a,l,c,d,h,u,g,m,f,b,w,k;for(e=e.replace(/^ +$/gm,"");e;)if((n=this.rules.newline.exec(e))&&(e=e.substring(n[0].length),n[0].length>1&&this.tokens.push({type:"space"})),n=this.rules.code.exec(e)){var x=this.tokens[this.tokens.length-1];e=e.substring(n[0].length),x&&"paragraph"===x.type?x.text+="\n"+n[0].trimRight():(n=n[0].replace(/^ {4}/gm,""),this.tokens.push({type:"code",codeBlockStyle:"indented",text:this.options.pedantic?n:v(n,"\n")}))}else if(n=this.rules.fences.exec(e))e=e.substring(n[0].length),this.tokens.push({type:"code",lang:n[2]?n[2].trim():n[2],text:n[3]||""});else if(n=this.rules.heading.exec(e))e=e.substring(n[0].length),this.tokens.push({type:"heading",depth:n[1].length,text:n[2]});else if((n=this.rules.nptable.exec(e))&&(l={type:"table",header:y(n[1].replace(/^ *| *\| *$/g,"")),align:n[2].replace(/^ *|\| *$/g,"").split(/ *\| */),cells:n[3]?n[3].replace(/\n$/,"").split("\n"):[]}).header.length===l.align.length){for(e=e.substring(n[0].length),g=0;g<l.align.length;g++)/^ *-+: *$/.test(l.align[g])?l.align[g]="right":/^ *:-+: *$/.test(l.align[g])?l.align[g]="center":/^ *:-+ *$/.test(l.align[g])?l.align[g]="left":l.align[g]=null;for(g=0;g<l.cells.length;g++)l.cells[g]=y(l.cells[g],l.header.length);this.tokens.push(l)}else if(n=this.rules.hr.exec(e))e=e.substring(n[0].length),this.tokens.push({type:"hr"});else if(n=this.rules.blockquote.exec(e))e=e.substring(n[0].length),this.tokens.push({type:"blockquote_start"}),n=n[0].replace(/^ *> ?/gm,""),this.token(n,t),this.tokens.push({type:"blockquote_end"});else if(n=this.rules.list.exec(e)){for(e=e.substring(n[0].length),c={type:"list_start",ordered:b=(s=n[2]).length>1,start:b?+s:"",loose:!1},this.tokens.push(c),d=[],r=!1,f=(n=n[0].match(this.rules.item)).length,g=0;g<f;g++)u=(l=n[g]).length,~(l=l.replace(/^ *([*+-]|\d+\.) */,"")).indexOf("\n ")&&(u-=l.length,l=this.options.pedantic?l.replace(/^ {1,4}/gm,""):l.replace(new RegExp("^ {1,"+u+"}","gm"),"")),g!==f-1&&(a=o.bullet.exec(n[g+1])[0],(s.length>1?1===a.length:a.length>1||this.options.smartLists&&a!==s)&&(e=n.slice(g+1).join("\n")+e,g=f-1)),i=r||/\n\n(?!\s*$)/.test(l),g!==f-1&&(r="\n"===l.charAt(l.length-1),i||(i=r)),i&&(c.loose=!0),k=void 0,(w=/^\[[ xX]\] /.test(l))&&(k=" "!==l[1],l=l.replace(/^\[[ xX]\] +/,"")),h={type:"list_item_start",task:w,checked:k,loose:i},d.push(h),this.tokens.push(h),this.token(l,!1),this.tokens.push({type:"list_item_end"});if(c.loose)for(f=d.length,g=0;g<f;g++)d[g].loose=!0;this.tokens.push({type:"list_end"})}else if(n=this.rules.html.exec(e))e=e.substring(n[0].length),this.tokens.push({type:this.options.sanitize?"paragraph":"html",pre:!this.options.sanitizer&&("pre"===n[1]||"script"===n[1]||"style"===n[1]),text:this.options.sanitize?this.options.sanitizer?this.options.sanitizer(n[0]):p(n[0]):n[0]});else if(t&&(n=this.rules.def.exec(e)))e=e.substring(n[0].length),n[3]&&(n[3]=n[3].substring(1,n[3].length-1)),m=n[1].toLowerCase().replace(/\s+/g," "),this.tokens.links[m]||(this.tokens.links[m]={href:n[2],title:n[3]});else if((n=this.rules.table.exec(e))&&(l={type:"table",header:y(n[1].replace(/^ *| *\| *$/g,"")),align:n[2].replace(/^ *|\| *$/g,"").split(/ *\| */),cells:n[3]?n[3].replace(/\n$/,"").split("\n"):[]}).header.length===l.align.length){for(e=e.substring(n[0].length),g=0;g<l.align.length;g++)/^ *-+: *$/.test(l.align[g])?l.align[g]="right":/^ *:-+: *$/.test(l.align[g])?l.align[g]="center":/^ *:-+ *$/.test(l.align[g])?l.align[g]="left":l.align[g]=null;for(g=0;g<l.cells.length;g++)l.cells[g]=y(l.cells[g].replace(/^ *\| *| *\| *$/g,""),l.header.length);this.tokens.push(l)}else if(n=this.rules.lheading.exec(e))e=e.substring(n[0].length),this.tokens.push({type:"heading",depth:"="===n[2].charAt(0)?1:2,text:n[1]});else if(t&&(n=this.rules.paragraph.exec(e)))e=e.substring(n[0].length),this.tokens.push({type:"paragraph",text:"\n"===n[1].charAt(n[1].length-1)?n[1].slice(0,-1):n[1]});else if(n=this.rules.text.exec(e))e=e.substring(n[0].length),this.tokens.push({type:"text",text:n[0]});else if(e)throw new Error("Infinite loop on byte: "+e.charCodeAt(0));return this.tokens};var i={escape:/^\\([!"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])/,autolink:/^<(scheme:[^\s\x00-\x1f<>]*|email)>/,url:f,tag:"^comment|^</[a-zA-Z][\\w:-]*\\s*>|^<[a-zA-Z][\\w-]*(?:attribute)*?\\s*/?>|^<\\?[\\s\\S]*?\\?>|^<![a-zA-Z]+\\s[\\s\\S]*?>|^<!\\[CDATA\\[[\\s\\S]*?\\]\\]>",link:/^!?\[(label)\]\(\s*(href)(?:\s+(title))?\s*\)/,reflink:/^!?\[(label)\]\[(?!\s*\])((?:\\[\[\]]?|[^\[\]\\])+)\]/,nolink:/^!?\[(?!\s*\])((?:\[[^\[\]]*\]|\\[\[\]]|[^\[\]])*)\](?:\[\])?/,strong:/^__([^\s_])__(?!_)|^\*\*([^\s*])\*\*(?!\*)|^__([^\s][\s\S]*?[^\s])__(?!_)|^\*\*([^\s][\s\S]*?[^\s])\*\*(?!\*)/,em:/^_([^\s_])_(?!_)|^\*([^\s*<\[])\*(?!\*)|^_([^\s<][\s\S]*?[^\s_])_(?!_|[^\spunctuation])|^_([^\s_<][\s\S]*?[^\s])_(?!_|[^\spunctuation])|^\*([^\s<"][\s\S]*?[^\s\*])\*(?!\*|[^\spunctuation])|^\*([^\s*"<\[][\s\S]*?[^\s])\*(?!\*)/,code:/^(`+)([^`]|[^`][\s\S]*?[^`])\1(?!`)/,br:/^( {2,}|\\)\n(?!\s*$)/,del:f,text:/^(`+|[^`])(?:[\s\S]*?(?:(?=[\\<!\[`*]|\b_|$)|[^ ](?= {2,}\n))|(?= {2,}\n))/};function n(e,t){if(this.options=t||x.defaults,this.links=e,this.rules=i.normal,this.renderer=this.options.renderer||new s,this.renderer.options=this.options,!this.links)throw new Error("Tokens array requires a `links` property.");this.options.pedantic?this.rules=i.pedantic:this.options.gfm&&(this.options.breaks?this.rules=i.breaks:this.rules=i.gfm)}function s(e){this.options=e||x.defaults}function a(){}function l(e){this.tokens=[],this.token=null,this.options=e||x.defaults,this.options.renderer=this.options.renderer||new s,this.renderer=this.options.renderer,this.renderer.options=this.options,this.slugger=new c}function c(){this.seen={}}function p(e,t){if(t){if(p.escapeTest.test(e))return e.replace(p.escapeReplace,(function(e){return p.replacements[e]}))}else if(p.escapeTestNoEncode.test(e))return e.replace(p.escapeReplaceNoEncode,(function(e){return p.replacements[e]}));return e}function d(e){return e.replace(/&(#(?:\d+)|(?:#x[0-9A-Fa-f]+)|(?:\w+));?/gi,(function(e,t){return"colon"===(t=t.toLowerCase())?":":"#"===t.charAt(0)?"x"===t.charAt(1)?String.fromCharCode(parseInt(t.substring(2),16)):String.fromCharCode(+t.substring(1)):""}))}function h(e,t){return e=e.source||e,t=t||"",{replace:function(t,o){return o=(o=o.source||o).replace(/(^|[^\[])\^/g,"$1"),e=e.replace(t,o),this},getRegex:function(){return new RegExp(e,t)}}}function u(e,t,o){if(e){try{var r=decodeURIComponent(d(o)).replace(/[^\w:]/g,"").toLowerCase()}catch(e){return null}if(0===r.indexOf("javascript:")||0===r.indexOf("vbscript:")||0===r.indexOf("data:"))return null}t&&!m.test(o)&&(o=function(e,t){g[" "+e]||(/^[^:]+:\/*[^/]*$/.test(e)?g[" "+e]=e+"/":g[" "+e]=v(e,"/",!0));return e=g[" "+e],"//"===t.slice(0,2)?e.replace(/:[\s\S]*/,":")+t:"/"===t.charAt(0)?e.replace(/(:\/*[^/]*)[\s\S]*/,"$1")+t:e+t}(t,o));try{o=encodeURI(o).replace(/%25/g,"%")}catch(e){return null}return o}i._punctuation="!\"#$%&'()*+,\\-./:;<=>?@\\[^_{|}~",i.em=h(i.em).replace(/punctuation/g,i._punctuation).getRegex(),i._escapes=/\\([!"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])/g,i._scheme=/[a-zA-Z][a-zA-Z0-9+.-]{1,31}/,i._email=/[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+(@)[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+(?![-_])/,i.autolink=h(i.autolink).replace("scheme",i._scheme).replace("email",i._email).getRegex(),i._attribute=/\s+[a-zA-Z:_][\w.:-]*(?:\s*=\s*"[^"]*"|\s*=\s*'[^']*'|\s*=\s*[^\s"'=<>`]+)?/,i.tag=h(i.tag).replace("comment",o._comment).replace("attribute",i._attribute).getRegex(),i._label=/(?:\[[^\[\]]*\]|\\.|`[^`]*`|[^\[\]\\`])*?/,i._href=/<(?:\\[<>]?|[^\s<>\\])*>|[^\s\x00-\x1f]*/,i._title=/"(?:\\"?|[^"\\])*"|'(?:\\'?|[^'\\])*'|\((?:\\\)?|[^)\\])*\)/,i.link=h(i.link).replace("label",i._label).replace("href",i._href).replace("title",i._title).getRegex(),i.reflink=h(i.reflink).replace("label",i._label).getRegex(),i.normal=b({},i),i.pedantic=b({},i.normal,{strong:/^__(?=\S)([\s\S]*?\S)__(?!_)|^\*\*(?=\S)([\s\S]*?\S)\*\*(?!\*)/,em:/^_(?=\S)([\s\S]*?\S)_(?!_)|^\*(?=\S)([\s\S]*?\S)\*(?!\*)/,link:h(/^!?\[(label)\]\((.*?)\)/).replace("label",i._label).getRegex(),reflink:h(/^!?\[(label)\]\s*\[([^\]]*)\]/).replace("label",i._label).getRegex()}),i.gfm=b({},i.normal,{escape:h(i.escape).replace("])","~|])").getRegex(),_extended_email:/[A-Za-z0-9._+-]+(@)[a-zA-Z0-9-_]+(?:\.[a-zA-Z0-9-_]*[a-zA-Z0-9])+(?![-_])/,url:/^((?:ftp|https?):\/\/|www\.)(?:[a-zA-Z0-9\-]+\.?)+[^\s<]*|^email/,_backpedal:/(?:[^?!.,:;*_~()&]+|\([^)]*\)|&(?![a-zA-Z0-9]+;$)|[?!.,:;*_~)]+(?!$))+/,del:/^~+(?=\S)([\s\S]*?\S)~+/,text:/^(`+|[^`])(?:[\s\S]*?(?:(?=[\\<!\[`*~]|\b_|https?:\/\/|ftp:\/\/|www\.|$)|[^ ](?= {2,}\n)|[^a-zA-Z0-9.!#$%&'*+\/=?_`{\|}~-](?=[a-zA-Z0-9.!#$%&'*+\/=?_`{\|}~-]+@))|(?= {2,}\n|[a-zA-Z0-9.!#$%&'*+\/=?_`{\|}~-]+@))/}),i.gfm.url=h(i.gfm.url,"i").replace("email",i.gfm._extended_email).getRegex(),i.breaks=b({},i.gfm,{br:h(i.br).replace("{2,}","*").getRegex(),text:h(i.gfm.text).replace("\\b_","\\b_| {2,}\\n").replace(/\{2,\}/g,"*").getRegex()}),n.rules=i,n.output=function(e,t,o){return new n(t,o).output(e)},n.prototype.output=function(e){for(var t,o,r,i,s,a,l="";e;)if(s=this.rules.escape.exec(e))e=e.substring(s[0].length),l+=p(s[1]);else if(s=this.rules.tag.exec(e))!this.inLink&&/^<a /i.test(s[0])?this.inLink=!0:this.inLink&&/^<\/a>/i.test(s[0])&&(this.inLink=!1),!this.inRawBlock&&/^<(pre|code|kbd|script)(\s|>)/i.test(s[0])?this.inRawBlock=!0:this.inRawBlock&&/^<\/(pre|code|kbd|script)(\s|>)/i.test(s[0])&&(this.inRawBlock=!1),e=e.substring(s[0].length),l+=this.options.sanitize?this.options.sanitizer?this.options.sanitizer(s[0]):p(s[0]):s[0];else if(s=this.rules.link.exec(e)){var c=w(s[2],"()");if(c>-1){var d=4+s[1].length+c;s[2]=s[2].substring(0,c),s[0]=s[0].substring(0,d).trim(),s[3]=""}e=e.substring(s[0].length),this.inLink=!0,r=s[2],this.options.pedantic?(t=/^([^'"]*[^\s])\s+(['"])(.*)\2/.exec(r))?(r=t[1],i=t[3]):i="":i=s[3]?s[3].slice(1,-1):"",r=r.trim().replace(/^<([\s\S]*)>$/,"$1"),l+=this.outputLink(s,{href:n.escapes(r),title:n.escapes(i)}),this.inLink=!1}else if((s=this.rules.reflink.exec(e))||(s=this.rules.nolink.exec(e))){if(e=e.substring(s[0].length),t=(s[2]||s[1]).replace(/\s+/g," "),!(t=this.links[t.toLowerCase()])||!t.href){l+=s[0].charAt(0),e=s[0].substring(1)+e;continue}this.inLink=!0,l+=this.outputLink(s,t),this.inLink=!1}else if(s=this.rules.strong.exec(e))e=e.substring(s[0].length),l+=this.renderer.strong(this.output(s[4]||s[3]||s[2]||s[1]));else if(s=this.rules.em.exec(e))e=e.substring(s[0].length),l+=this.renderer.em(this.output(s[6]||s[5]||s[4]||s[3]||s[2]||s[1]));else if(s=this.rules.code.exec(e))e=e.substring(s[0].length),l+=this.renderer.codespan(p(s[2].trim(),!0));else if(s=this.rules.br.exec(e))e=e.substring(s[0].length),l+=this.renderer.br();else if(s=this.rules.del.exec(e))e=e.substring(s[0].length),l+=this.renderer.del(this.output(s[1]));else if(s=this.rules.autolink.exec(e))e=e.substring(s[0].length),r="@"===s[2]?"mailto:"+(o=p(this.mangle(s[1]))):o=p(s[1]),l+=this.renderer.link(r,null,o);else if(this.inLink||!(s=this.rules.url.exec(e))){if(s=this.rules.text.exec(e))e=e.substring(s[0].length),this.inRawBlock?l+=this.renderer.text(this.options.sanitize?this.options.sanitizer?this.options.sanitizer(s[0]):p(s[0]):s[0]):l+=this.renderer.text(p(this.smartypants(s[0])));else if(e)throw new Error("Infinite loop on byte: "+e.charCodeAt(0))}else{if("@"===s[2])r="mailto:"+(o=p(s[0]));else{do{a=s[0],s[0]=this.rules._backpedal.exec(s[0])[0]}while(a!==s[0]);o=p(s[0]),r="www."===s[1]?"http://"+o:o}e=e.substring(s[0].length),l+=this.renderer.link(r,null,o)}return l},n.escapes=function(e){return e?e.replace(n.rules._escapes,"$1"):e},n.prototype.outputLink=function(e,t){var o=t.href,r=t.title?p(t.title):null;return"!"!==e[0].charAt(0)?this.renderer.link(o,r,this.output(e[1])):this.renderer.image(o,r,p(e[1]))},n.prototype.smartypants=function(e){return this.options.smartypants?e.replace(/---/g,"—").replace(/--/g,"–").replace(/(^|[-\u2014/(\[{"\s])'/g,"$1‘").replace(/'/g,"’").replace(/(^|[-\u2014/(\[{\u2018\s])"/g,"$1“").replace(/"/g,"”").replace(/\.{3}/g,"…"):e},n.prototype.mangle=function(e){if(!this.options.mangle)return e;for(var t,o="",r=e.length,i=0;i<r;i++)t=e.charCodeAt(i),Math.random()>.5&&(t="x"+t.toString(16)),o+="&#"+t+";";return o},s.prototype.code=function(e,t,o){var r=(t||"").match(/\S*/)[0];if(this.options.highlight){var i=this.options.highlight(e,r);null!=i&&i!==e&&(o=!0,e=i)}return r?'<pre><code class="'+this.options.langPrefix+p(r,!0)+'">'+(o?e:p(e,!0))+"</code></pre>\n":"<pre><code>"+(o?e:p(e,!0))+"</code></pre>"},s.prototype.blockquote=function(e){return"<blockquote>\n"+e+"</blockquote>\n"},s.prototype.html=function(e){return e},s.prototype.heading=function(e,t,o,r){return this.options.headerIds?"<h"+t+' id="'+this.options.headerPrefix+r.slug(o)+'">'+e+"</h"+t+">\n":"<h"+t+">"+e+"</h"+t+">\n"},s.prototype.hr=function(){return this.options.xhtml?"<hr/>\n":"<hr>\n"},s.prototype.list=function(e,t,o){var r=t?"ol":"ul";return"<"+r+(t&&1!==o?' start="'+o+'"':"")+">\n"+e+"</"+r+">\n"},s.prototype.listitem=function(e){return"<li>"+e+"</li>\n"},s.prototype.checkbox=function(e){return"<input "+(e?'checked="" ':"")+'disabled="" type="checkbox"'+(this.options.xhtml?" /":"")+"> "},s.prototype.paragraph=function(e){return"<p>"+e+"</p>\n"},s.prototype.table=function(e,t){return t&&(t="<tbody>"+t+"</tbody>"),"<table>\n<thead>\n"+e+"</thead>\n"+t+"</table>\n"},s.prototype.tablerow=function(e){return"<tr>\n"+e+"</tr>\n"},s.prototype.tablecell=function(e,t){var o=t.header?"th":"td";return(t.align?"<"+o+' align="'+t.align+'">':"<"+o+">")+e+"</"+o+">\n"},s.prototype.strong=function(e){return"<strong>"+e+"</strong>"},s.prototype.em=function(e){return"<em>"+e+"</em>"},s.prototype.codespan=function(e){return"<code>"+e+"</code>"},s.prototype.br=function(){return this.options.xhtml?"<br/>":"<br>"},s.prototype.del=function(e){return"<del>"+e+"</del>"},s.prototype.link=function(e,t,o){if(null===(e=u(this.options.sanitize,this.options.baseUrl,e)))return o;var r='<a href="'+p(e)+'"';return t&&(r+=' title="'+t+'"'),r+=">"+o+"</a>"},s.prototype.image=function(e,t,o){if(null===(e=u(this.options.sanitize,this.options.baseUrl,e)))return o;var r='<img src="'+e+'" alt="'+o+'"';return t&&(r+=' title="'+t+'"'),r+=this.options.xhtml?"/>":">"},s.prototype.text=function(e){return e},a.prototype.strong=a.prototype.em=a.prototype.codespan=a.prototype.del=a.prototype.text=function(e){return e},a.prototype.link=a.prototype.image=function(e,t,o){return""+o},a.prototype.br=function(){return""},l.parse=function(e,t){return new l(t).parse(e)},l.prototype.parse=function(e){this.inline=new n(e.links,this.options),this.inlineText=new n(e.links,b({},this.options,{renderer:new a})),this.tokens=e.reverse();for(var t="";this.next();)t+=this.tok();return t},l.prototype.next=function(){return this.token=this.tokens.pop(),this.token},l.prototype.peek=function(){return this.tokens[this.tokens.length-1]||0},l.prototype.parseText=function(){for(var e=this.token.text;"text"===this.peek().type;)e+="\n"+this.next().text;return this.inline.output(e)},l.prototype.tok=function(){switch(this.token.type){case"space":return"";case"hr":return this.renderer.hr();case"heading":return this.renderer.heading(this.inline.output(this.token.text),this.token.depth,d(this.inlineText.output(this.token.text)),this.slugger);case"code":return this.renderer.code(this.token.text,this.token.lang,this.token.escaped);case"table":var e,t,o,r,i="",n="";for(o="",e=0;e<this.token.header.length;e++)o+=this.renderer.tablecell(this.inline.output(this.token.header[e]),{header:!0,align:this.token.align[e]});for(i+=this.renderer.tablerow(o),e=0;e<this.token.cells.length;e++){for(t=this.token.cells[e],o="",r=0;r<t.length;r++)o+=this.renderer.tablecell(this.inline.output(t[r]),{header:!1,align:this.token.align[r]});n+=this.renderer.tablerow(o)}return this.renderer.table(i,n);case"blockquote_start":for(n="";"blockquote_end"!==this.next().type;)n+=this.tok();return this.renderer.blockquote(n);case"list_start":n="";for(var s=this.token.ordered,a=this.token.start;"list_end"!==this.next().type;)n+=this.tok();return this.renderer.list(n,s,a);case"list_item_start":n="";var l=this.token.loose,c=this.token.checked,p=this.token.task;for(this.token.task&&(n+=this.renderer.checkbox(c));"list_item_end"!==this.next().type;)n+=l||"text"!==this.token.type?this.tok():this.parseText();return this.renderer.listitem(n,p,c);case"html":return this.renderer.html(this.token.text);case"paragraph":return this.renderer.paragraph(this.inline.output(this.token.text));case"text":return this.renderer.paragraph(this.parseText());default:var h='Token with "'+this.token.type+'" type was not found.';if(!this.options.silent)throw new Error(h);console.log(h)}},c.prototype.slug=function(e){var t=e.toLowerCase().trim().replace(/[\u2000-\u206F\u2E00-\u2E7F\\'!"#$%&()*+,./:;<=>?@[\]^`{|}~]/g,"").replace(/\s/g,"-");if(this.seen.hasOwnProperty(t)){var o=t;do{this.seen[o]++,t=o+"-"+this.seen[o]}while(this.seen.hasOwnProperty(t))}return this.seen[t]=0,t},p.escapeTest=/[&<>"']/,p.escapeReplace=/[&<>"']/g,p.replacements={"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"},p.escapeTestNoEncode=/[<>"']|&(?!#?\w+;)/,p.escapeReplaceNoEncode=/[<>"']|&(?!#?\w+;)/g;var g={},m=/^$|^[a-z][a-z0-9+.-]*:|^[?#]/i;function f(){}function b(e){for(var t,o,r=1;r<arguments.length;r++)for(o in t=arguments[r])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e}function y(e,t){var o=e.replace(/\|/g,(function(e,t,o){for(var r=!1,i=t;--i>=0&&"\\"===o[i];)r=!r;return r?"|":" |"})).split(/ \|/),r=0;if(o.length>t)o.splice(t);else for(;o.length<t;)o.push("");for(;r<o.length;r++)o[r]=o[r].trim().replace(/\\\|/g,"|");return o}function v(e,t,o){if(0===e.length)return"";for(var r=0;r<e.length;){var i=e.charAt(e.length-r-1);if(i!==t||o){if(i===t||!o)break;r++}else r++}return e.substr(0,e.length-r)}function w(e,t){if(-1===e.indexOf(t[1]))return-1;for(var o=0,r=0;r<e.length;r++)if("\\"===e[r])r++;else if(e[r]===t[0])o++;else if(e[r]===t[1]&&--o<0)return r;return-1}function k(e){e&&e.sanitize&&!e.silent&&console.warn("marked(): sanitize and sanitizer parameters are deprecated since version 0.7.0, should not be used and will be removed in the future. Read more here: https://marked.js.org/#/USING_ADVANCED.md#options")}function x(e,t,o){if(null==e)throw new Error("marked(): input parameter is undefined or null");if("string"!=typeof e)throw new Error("marked(): input parameter is of type "+Object.prototype.toString.call(e)+", string expected");if(o||"function"==typeof t){o||(o=t,t=null),k(t=b({},x.defaults,t||{}));var i,n,s=t.highlight,a=0;try{i=r.lex(e,t)}catch(e){return o(e)}n=i.length;var c=function(e){if(e)return t.highlight=s,o(e);var r;try{r=l.parse(i,t)}catch(t){e=t}return t.highlight=s,e?o(e):o(null,r)};if(!s||s.length<3)return c();if(delete t.highlight,!n)return c();for(;a<i.length;a++)!function(e){"code"!==e.type?--n||c():s(e.text,e.lang,(function(t,o){return t?c(t):null==o||o===e.text?--n||c():(e.text=o,e.escaped=!0,void(--n||c()))}))}(i[a])}else try{return t&&(t=b({},x.defaults,t)),k(t),l.parse(r.lex(e,t),t)}catch(e){if(e.message+="\nPlease report this to https://github.com/markedjs/marked.",(t||x.defaults).silent)return"<p>An error occurred:</p><pre>"+p(e.message+"",!0)+"</pre>";throw e}}f.exec=f,x.options=x.setOptions=function(e){return b(x.defaults,e),x},x.getDefaults=function(){return{baseUrl:null,breaks:!1,gfm:!0,headerIds:!0,headerPrefix:"",highlight:null,langPrefix:"language-",mangle:!0,pedantic:!1,renderer:new s,sanitize:!1,sanitizer:null,silent:!1,smartLists:!1,smartypants:!1,xhtml:!1}},x.defaults=x.getDefaults(),x.Parser=l,x.parser=l.parse,x.Renderer=s,x.TextRenderer=a,x.Lexer=r,x.lexer=r.lex,x.InlineLexer=n,x.inlineLexer=n.output,x.Slugger=c,x.parse=x,e.exports=x}()}));function _e(){var e={"align-content":!1,"align-items":!1,"align-self":!1,"alignment-adjust":!1,"alignment-baseline":!1,all:!1,"anchor-point":!1,animation:!1,"animation-delay":!1,"animation-direction":!1,"animation-duration":!1,"animation-fill-mode":!1,"animation-iteration-count":!1,"animation-name":!1,"animation-play-state":!1,"animation-timing-function":!1,azimuth:!1,"backface-visibility":!1,background:!0,"background-attachment":!0,"background-clip":!0,"background-color":!0,"background-image":!0,"background-origin":!0,"background-position":!0,"background-repeat":!0,"background-size":!0,"baseline-shift":!1,binding:!1,bleed:!1,"bookmark-label":!1,"bookmark-level":!1,"bookmark-state":!1,border:!0,"border-bottom":!0,"border-bottom-color":!0,"border-bottom-left-radius":!0,"border-bottom-right-radius":!0,"border-bottom-style":!0,"border-bottom-width":!0,"border-collapse":!0,"border-color":!0,"border-image":!0,"border-image-outset":!0,"border-image-repeat":!0,"border-image-slice":!0,"border-image-source":!0,"border-image-width":!0,"border-left":!0,"border-left-color":!0,"border-left-style":!0,"border-left-width":!0,"border-radius":!0,"border-right":!0,"border-right-color":!0,"border-right-style":!0,"border-right-width":!0,"border-spacing":!0,"border-style":!0,"border-top":!0,"border-top-color":!0,"border-top-left-radius":!0,"border-top-right-radius":!0,"border-top-style":!0,"border-top-width":!0,"border-width":!0,bottom:!1,"box-decoration-break":!0,"box-shadow":!0,"box-sizing":!0,"box-snap":!0,"box-suppress":!0,"break-after":!0,"break-before":!0,"break-inside":!0,"caption-side":!1,chains:!1,clear:!0,clip:!1,"clip-path":!1,"clip-rule":!1,color:!0,"color-interpolation-filters":!0,"column-count":!1,"column-fill":!1,"column-gap":!1,"column-rule":!1,"column-rule-color":!1,"column-rule-style":!1,"column-rule-width":!1,"column-span":!1,"column-width":!1,columns:!1,contain:!1,content:!1,"counter-increment":!1,"counter-reset":!1,"counter-set":!1,crop:!1,cue:!1,"cue-after":!1,"cue-before":!1,cursor:!1,direction:!1,display:!0,"display-inside":!0,"display-list":!0,"display-outside":!0,"dominant-baseline":!1,elevation:!1,"empty-cells":!1,filter:!1,flex:!1,"flex-basis":!1,"flex-direction":!1,"flex-flow":!1,"flex-grow":!1,"flex-shrink":!1,"flex-wrap":!1,float:!1,"float-offset":!1,"flood-color":!1,"flood-opacity":!1,"flow-from":!1,"flow-into":!1,font:!0,"font-family":!0,"font-feature-settings":!0,"font-kerning":!0,"font-language-override":!0,"font-size":!0,"font-size-adjust":!0,"font-stretch":!0,"font-style":!0,"font-synthesis":!0,"font-variant":!0,"font-variant-alternates":!0,"font-variant-caps":!0,"font-variant-east-asian":!0,"font-variant-ligatures":!0,"font-variant-numeric":!0,"font-variant-position":!0,"font-weight":!0,grid:!1,"grid-area":!1,"grid-auto-columns":!1,"grid-auto-flow":!1,"grid-auto-rows":!1,"grid-column":!1,"grid-column-end":!1,"grid-column-start":!1,"grid-row":!1,"grid-row-end":!1,"grid-row-start":!1,"grid-template":!1,"grid-template-areas":!1,"grid-template-columns":!1,"grid-template-rows":!1,"hanging-punctuation":!1,height:!0,hyphens:!1,icon:!1,"image-orientation":!1,"image-resolution":!1,"ime-mode":!1,"initial-letters":!1,"inline-box-align":!1,"justify-content":!1,"justify-items":!1,"justify-self":!1,left:!1,"letter-spacing":!0,"lighting-color":!0,"line-box-contain":!1,"line-break":!1,"line-grid":!1,"line-height":!1,"line-snap":!1,"line-stacking":!1,"line-stacking-ruby":!1,"line-stacking-shift":!1,"line-stacking-strategy":!1,"list-style":!0,"list-style-image":!0,"list-style-position":!0,"list-style-type":!0,margin:!0,"margin-bottom":!0,"margin-left":!0,"margin-right":!0,"margin-top":!0,"marker-offset":!1,"marker-side":!1,marks:!1,mask:!1,"mask-box":!1,"mask-box-outset":!1,"mask-box-repeat":!1,"mask-box-slice":!1,"mask-box-source":!1,"mask-box-width":!1,"mask-clip":!1,"mask-image":!1,"mask-origin":!1,"mask-position":!1,"mask-repeat":!1,"mask-size":!1,"mask-source-type":!1,"mask-type":!1,"max-height":!0,"max-lines":!1,"max-width":!0,"min-height":!0,"min-width":!0,"move-to":!1,"nav-down":!1,"nav-index":!1,"nav-left":!1,"nav-right":!1,"nav-up":!1,"object-fit":!1,"object-position":!1,opacity:!1,order:!1,orphans:!1,outline:!1,"outline-color":!1,"outline-offset":!1,"outline-style":!1,"outline-width":!1,overflow:!1,"overflow-wrap":!1,"overflow-x":!1,"overflow-y":!1,padding:!0,"padding-bottom":!0,"padding-left":!0,"padding-right":!0,"padding-top":!0,page:!1,"page-break-after":!1,"page-break-before":!1,"page-break-inside":!1,"page-policy":!1,pause:!1,"pause-after":!1,"pause-before":!1,perspective:!1,"perspective-origin":!1,pitch:!1,"pitch-range":!1,"play-during":!1,position:!1,"presentation-level":!1,quotes:!1,"region-fragment":!1,resize:!1,rest:!1,"rest-after":!1,"rest-before":!1,richness:!1,right:!1,rotation:!1,"rotation-point":!1,"ruby-align":!1,"ruby-merge":!1,"ruby-position":!1,"shape-image-threshold":!1,"shape-outside":!1,"shape-margin":!1,size:!1,speak:!1,"speak-as":!1,"speak-header":!1,"speak-numeral":!1,"speak-punctuation":!1,"speech-rate":!1,stress:!1,"string-set":!1,"tab-size":!1,"table-layout":!1,"text-align":!0,"text-align-last":!0,"text-combine-upright":!0,"text-decoration":!0,"text-decoration-color":!0,"text-decoration-line":!0,"text-decoration-skip":!0,"text-decoration-style":!0,"text-emphasis":!0,"text-emphasis-color":!0,"text-emphasis-position":!0,"text-emphasis-style":!0,"text-height":!0,"text-indent":!0,"text-justify":!0,"text-orientation":!0,"text-overflow":!0,"text-shadow":!0,"text-space-collapse":!0,"text-transform":!0,"text-underline-position":!0,"text-wrap":!0,top:!1,transform:!1,"transform-origin":!1,"transform-style":!1,transition:!1,"transition-delay":!1,"transition-duration":!1,"transition-property":!1,"transition-timing-function":!1,"unicode-bidi":!1,"vertical-align":!1,visibility:!1,"voice-balance":!1,"voice-duration":!1,"voice-family":!1,"voice-pitch":!1,"voice-range":!1,"voice-rate":!1,"voice-stress":!1,"voice-volume":!1,volume:!1,"white-space":!1,widows:!1,width:!0,"will-change":!1,"word-break":!0,"word-spacing":!0,"word-wrap":!0,"wrap-flow":!1,"wrap-through":!1,"writing-mode":!1,"z-index":!1};return e}var Ae=/javascript\s*\:/gim;var Se={whiteList:_e(),getDefaultWhiteList:_e,onAttr:function(e,t,o){},onIgnoreAttr:function(e,t,o){},safeAttrValue:function(e,t){return Ae.test(t)?"":t}},$e={indexOf:function(e,t){var o,r;if(Array.prototype.indexOf)return e.indexOf(t);for(o=0,r=e.length;o<r;o++)if(e[o]===t)return o;return-1},forEach:function(e,t,o){var r,i;if(Array.prototype.forEach)return e.forEach(t,o);for(r=0,i=e.length;r<i;r++)t.call(o,e[r],r,e)},trim:function(e){return String.prototype.trim?e.trim():e.replace(/(^\s*)|(\s*$)/g,"")},trimRight:function(e){return String.prototype.trimRight?e.trimRight():e.replace(/(\s*$)/g,"")}};var Ee=function(e,t){";"!==(e=$e.trimRight(e))[e.length-1]&&(e+=";");var o=e.length,r=!1,i=0,n=0,s="";function a(){if(!r){var o=$e.trim(e.slice(i,n)),a=o.indexOf(":");if(-1!==a){var l=$e.trim(o.slice(0,a)),c=$e.trim(o.slice(a+1));if(l){var p=t(i,s.length,l,c,o);p&&(s+=p+"; ")}}}i=n+1}for(;n<o;n++){var l=e[n];if("/"===l&&"*"===e[n+1]){var c=e.indexOf("*/",n+2);if(-1===c)break;i=(n=c+1)+1,r=!1}else"("===l?r=!0:")"===l?r=!1:";"===l?r||a():"\n"===l&&a()}return $e.trim(s)};function ze(e){return null==e}function Ce(e){(e=function(e){var t={};for(var o in e)t[o]=e[o];return t}(e||{})).whiteList=e.whiteList||Se.whiteList,e.onAttr=e.onAttr||Se.onAttr,e.onIgnoreAttr=e.onIgnoreAttr||Se.onIgnoreAttr,e.safeAttrValue=e.safeAttrValue||Se.safeAttrValue,this.options=e}Ce.prototype.process=function(e){if(!(e=(e=e||"").toString()))return"";var t=this.options,o=t.whiteList,r=t.onAttr,i=t.onIgnoreAttr,n=t.safeAttrValue;return Ee(e,(function(e,t,s,a,l){var c=o[s],p=!1;if(!0===c?p=c:"function"==typeof c?p=c(a):c instanceof RegExp&&(p=c.test(a)),!0!==p&&(p=!1),a=n(s,a)){var d,h={position:t,sourcePosition:e,source:l,isWhite:p};return p?ze(d=r(s,a,h))?s+":"+a:d:ze(d=i(s,a,h))?void 0:d}}))};var Te=Ce,Re=ke((function(e,t){for(var o in(t=e.exports=function(e,t){return new Te(t).process(e)}).FilterCSS=Te,Se)t[o]=Se[o];"undefined"!=typeof window&&(window.filterCSS=e.exports)})),Ne=(Re.FilterCSS,{indexOf:function(e,t){var o,r;if(Array.prototype.indexOf)return e.indexOf(t);for(o=0,r=e.length;o<r;o++)if(e[o]===t)return o;return-1},forEach:function(e,t,o){var r,i;if(Array.prototype.forEach)return e.forEach(t,o);for(r=0,i=e.length;r<i;r++)t.call(o,e[r],r,e)},trim:function(e){return String.prototype.trim?e.trim():e.replace(/(^\s*)|(\s*$)/g,"")},spaceIndex:function(e){var t=/\s|\n|\t/.exec(e);return t?t.index:-1}}),Me=Re.FilterCSS,Pe=Re.getDefaultWhiteList;function Le(){return{a:["target","href","title"],abbr:["title"],address:[],area:["shape","coords","href","alt"],article:[],aside:[],audio:["autoplay","controls","loop","preload","src"],b:[],bdi:["dir"],bdo:["dir"],big:[],blockquote:["cite"],br:[],caption:[],center:[],cite:[],code:[],col:["align","valign","span","width"],colgroup:["align","valign","span","width"],dd:[],del:["datetime"],details:["open"],div:[],dl:[],dt:[],em:[],font:["color","size","face"],footer:[],h1:[],h2:[],h3:[],h4:[],h5:[],h6:[],header:[],hr:[],i:[],img:["src","alt","title","width","height"],ins:["datetime"],li:[],mark:[],nav:[],ol:[],p:[],pre:[],s:[],section:[],small:[],span:[],sub:[],sup:[],strong:[],table:["width","border","align","valign"],tbody:["align","valign"],td:["width","rowspan","colspan","align","valign"],tfoot:["align","valign"],th:["width","rowspan","colspan","align","valign"],thead:["align","valign"],tr:["rowspan","align","valign"],tt:[],u:[],ul:[],video:["autoplay","controls","loop","preload","src","height","width"]}}var Ie=new Me;function Be(e){return e.replace(Oe,"&lt;").replace(De,"&gt;")}var Oe=/</g,De=/>/g,je=/"/g,Ue=/&quot;/g,Ve=/&#([a-zA-Z0-9]*);?/gim,He=/&colon;?/gim,qe=/&newline;?/gim,Fe=/((j\s*a\s*v\s*a|v\s*b|l\s*i\s*v\s*e)\s*s\s*c\s*r\s*i\s*p\s*t\s*|m\s*o\s*c\s*h\s*a)\:/gi,Ge=/e\s*x\s*p\s*r\s*e\s*s\s*s\s*i\s*o\s*n\s*\(.*/gi,Ze=/u\s*r\s*l\s*\(.*/gi;function Ye(e){return e.replace(je,"&quot;")}function We(e){return e.replace(Ue,'"')}function Qe(e){return e.replace(Ve,(function(e,t){return"x"===t[0]||"X"===t[0]?String.fromCharCode(parseInt(t.substr(1),16)):String.fromCharCode(parseInt(t,10))}))}function Ke(e){return e.replace(He,":").replace(qe," ")}function Xe(e){for(var t="",o=0,r=e.length;o<r;o++)t+=e.charCodeAt(o)<32?" ":e.charAt(o);return Ne.trim(t)}function Je(e){return e=Xe(e=Ke(e=Qe(e=We(e))))}function et(e){return e=Be(e=Ye(e))}var tt=/<!--[\s\S]*?-->/g;var ot={whiteList:{a:["target","href","title"],abbr:["title"],address:[],area:["shape","coords","href","alt"],article:[],aside:[],audio:["autoplay","controls","loop","preload","src"],b:[],bdi:["dir"],bdo:["dir"],big:[],blockquote:["cite"],br:[],caption:[],center:[],cite:[],code:[],col:["align","valign","span","width"],colgroup:["align","valign","span","width"],dd:[],del:["datetime"],details:["open"],div:[],dl:[],dt:[],em:[],font:["color","size","face"],footer:[],h1:[],h2:[],h3:[],h4:[],h5:[],h6:[],header:[],hr:[],i:[],img:["src","alt","title","width","height"],ins:["datetime"],li:[],mark:[],nav:[],ol:[],p:[],pre:[],s:[],section:[],small:[],span:[],sub:[],sup:[],strong:[],table:["width","border","align","valign"],tbody:["align","valign"],td:["width","rowspan","colspan","align","valign"],tfoot:["align","valign"],th:["width","rowspan","colspan","align","valign"],thead:["align","valign"],tr:["rowspan","align","valign"],tt:[],u:[],ul:[],video:["autoplay","controls","loop","preload","src","height","width"]},getDefaultWhiteList:Le,onTag:function(e,t,o){},onIgnoreTag:function(e,t,o){},onTagAttr:function(e,t,o){},onIgnoreTagAttr:function(e,t,o){},safeAttrValue:function(e,t,o,r){if(o=Je(o),"href"===t||"src"===t){if("#"===(o=Ne.trim(o)))return"#";if("http://"!==o.substr(0,7)&&"https://"!==o.substr(0,8)&&"mailto:"!==o.substr(0,7)&&"tel:"!==o.substr(0,4)&&"#"!==o[0]&&"/"!==o[0])return""}else if("background"===t){if(Fe.lastIndex=0,Fe.test(o))return""}else if("style"===t){if(Ge.lastIndex=0,Ge.test(o))return"";if(Ze.lastIndex=0,Ze.test(o)&&(Fe.lastIndex=0,Fe.test(o)))return"";!1!==r&&(o=(r=r||Ie).process(o))}return o=et(o)},escapeHtml:Be,escapeQuote:Ye,unescapeQuote:We,escapeHtmlEntities:Qe,escapeDangerHtml5Entities:Ke,clearNonPrintableCharacter:Xe,friendlyAttrValue:Je,escapeAttrValue:et,onIgnoreTagStripAll:function(){return""},StripTagBody:function(e,t){"function"!=typeof t&&(t=function(){});var o=!Array.isArray(e),r=[],i=!1;return{onIgnoreTag:function(n,s,a){if(function(t){return!!o||-1!==Ne.indexOf(e,t)}(n)){if(a.isClosing){var l="[/removed]",c=a.position+l.length;return r.push([!1!==i?i:a.position,c]),i=!1,l}return i||(i=a.position),"[removed]"}return t(n,s,a)},remove:function(e){var t="",o=0;return Ne.forEach(r,(function(r){t+=e.slice(o,r[0]),o=r[1]})),t+=e.slice(o)}}},stripCommentTag:function(e){return e.replace(tt,"")},stripBlankChar:function(e){var t=e.split("");return(t=t.filter((function(e){var t=e.charCodeAt(0);return 127!==t&&(!(t<=31)||(10===t||13===t))}))).join("")},cssFilter:Ie,getDefaultCSSWhiteList:Pe};function rt(e){var t=Ne.spaceIndex(e);if(-1===t)var o=e.slice(1,-1);else o=e.slice(1,t+1);return"/"===(o=Ne.trim(o).toLowerCase()).slice(0,1)&&(o=o.slice(1)),"/"===o.slice(-1)&&(o=o.slice(0,-1)),o}function it(e){return"</"===e.slice(0,2)}var nt=/[^a-zA-Z0-9_:\.\-]/gim;function st(e,t){for(;t<e.length;t++){var o=e[t];if(" "!==o)return"="===o?t:-1}}function at(e,t){for(;t>0;t--){var o=e[t];if(" "!==o)return"="===o?t:-1}}function lt(e){return function(e){return'"'===e[0]&&'"'===e[e.length-1]||"'"===e[0]&&"'"===e[e.length-1]}(e)?e.substr(1,e.length-2):e}var ct={parseTag:function(e,t,o){var r="",i=0,n=!1,s=!1,a=0,l=e.length,c="",p="";for(a=0;a<l;a++){var d=e.charAt(a);if(!1===n){if("<"===d){n=a;continue}}else if(!1===s){if("<"===d){r+=o(e.slice(i,a)),n=a,i=a;continue}if(">"===d){r+=o(e.slice(i,n)),c=rt(p=e.slice(n,a+1)),r+=t(n,r.length,c,p,it(p)),i=a+1,n=!1;continue}if(('"'===d||"'"===d)&&"="===e.charAt(a-1)){s=d;continue}}else if(d===s){s=!1;continue}}return i<e.length&&(r+=o(e.substr(i))),r},parseAttr:function(e,t){var o=0,r=[],i=!1,n=e.length;function s(e,o){if(!((e=(e=Ne.trim(e)).replace(nt,"").toLowerCase()).length<1)){var i=t(e,o||"");i&&r.push(i)}}for(var a=0;a<n;a++){var l,c=e.charAt(a);if(!1!==i||"="!==c)if(!1===i||a!==o||'"'!==c&&"'"!==c||"="!==e.charAt(a-1))if(/\s|\n|\t/.test(c)){if(e=e.replace(/\s|\n|\t/g," "),!1===i){if(-1===(l=st(e,a))){s(Ne.trim(e.slice(o,a))),i=!1,o=a+1;continue}a=l-1;continue}if(-1===(l=at(e,a-1))){s(i,lt(Ne.trim(e.slice(o,a)))),i=!1,o=a+1;continue}}else;else{if(-1===(l=e.indexOf(c,a+1)))break;s(i,Ne.trim(e.slice(o+1,l))),i=!1,o=(a=l)+1}else i=e.slice(o,a),o=a+1}return o<e.length&&(!1===i?s(e.slice(o)):s(i,lt(Ne.trim(e.slice(o))))),Ne.trim(r.join(" "))}},pt=Re.FilterCSS,dt=ct.parseTag,ht=ct.parseAttr;function ut(e){return null==e}function gt(e){(e=function(e){var t={};for(var o in e)t[o]=e[o];return t}(e||{})).stripIgnoreTag&&(e.onIgnoreTag&&console.error('Notes: cannot use these two options "stripIgnoreTag" and "onIgnoreTag" at the same time'),e.onIgnoreTag=ot.onIgnoreTagStripAll),e.whiteList=e.whiteList||ot.whiteList,e.onTag=e.onTag||ot.onTag,e.onTagAttr=e.onTagAttr||ot.onTagAttr,e.onIgnoreTag=e.onIgnoreTag||ot.onIgnoreTag,e.onIgnoreTagAttr=e.onIgnoreTagAttr||ot.onIgnoreTagAttr,e.safeAttrValue=e.safeAttrValue||ot.safeAttrValue,e.escapeHtml=e.escapeHtml||ot.escapeHtml,this.options=e,!1===e.css?this.cssFilter=!1:(e.css=e.css||{},this.cssFilter=new pt(e.css))}gt.prototype.process=function(e){if(!(e=(e=e||"").toString()))return"";var t=this.options,o=t.whiteList,r=t.onTag,i=t.onIgnoreTag,n=t.onTagAttr,s=t.onIgnoreTagAttr,a=t.safeAttrValue,l=t.escapeHtml,c=this.cssFilter;t.stripBlankChar&&(e=ot.stripBlankChar(e)),t.allowCommentTag||(e=ot.stripCommentTag(e));var p=!1;if(t.stripIgnoreTagBody){p=ot.StripTagBody(t.stripIgnoreTagBody,i);i=p.onIgnoreTag}var d=dt(e,(function(e,t,p,d,h){var u,g={sourcePosition:e,position:t,isClosing:h,isWhite:o.hasOwnProperty(p)};if(!ut(u=r(p,d,g)))return u;if(g.isWhite){if(g.isClosing)return"</"+p+">";var m=function(e){var t=Ne.spaceIndex(e);if(-1===t)return{html:"",closing:"/"===e[e.length-2]};var o="/"===(e=Ne.trim(e.slice(t+1,-1)))[e.length-1];return o&&(e=Ne.trim(e.slice(0,-1))),{html:e,closing:o}}(d),f=o[p],b=ht(m.html,(function(e,t){var o,r=-1!==Ne.indexOf(f,e);return ut(o=n(p,e,t,r))?r?(t=a(p,e,t,c))?e+'="'+t+'"':e:ut(o=s(p,e,t,r))?void 0:o:o}));d="<"+p;return b&&(d+=" "+b),m.closing&&(d+=" /"),d+=">"}return ut(u=i(p,d,g))?l(d):u}),l);return p&&(d=p.remove(d)),d};var mt=gt,ft=ke((function(e,t){function o(e,t){return new mt(t).process(e)}for(var r in(t=e.exports=o).filterXSS=o,t.FilterXSS=mt,ot)t[r]=ot[r];for(var r in ct)t[r]=ct[r];"undefined"!=typeof window&&(window.filterXSS=e.exports),"undefined"!=typeof self&&"undefined"!=typeof DedicatedWorkerGlobalScope&&self instanceof DedicatedWorkerGlobalScope&&(self.filterXSS=e.exports)})),bt=ft.filterXSS,yt=(ft.FilterXSS,ke((function(e,t){var o,r;o=function(e){var t=[],o=Object.keys,r={},i={},n=/^(no-?highlight|plain|text)$/i,s=/\blang(?:uage)?-([\w-]+)\b/i,a=/((^(<[^>]+>|\t|)+|(?:\n)))/gm,l="</span>",c={classPrefix:"hljs-",tabReplace:null,useBR:!1,languages:void 0},p="of and for in not or if then".split(" ");function d(e){return e.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}function h(e){return e.nodeName.toLowerCase()}function u(e){return n.test(e)}function g(e){var t,o={},r=Array.prototype.slice.call(arguments,1);for(t in e)o[t]=e[t];return r.forEach((function(e){for(t in e)o[t]=e[t]})),o}function m(e){var t=[];return function e(o,r){for(var i=o.firstChild;i;i=i.nextSibling)3===i.nodeType?r+=i.nodeValue.length:1===i.nodeType&&(t.push({event:"start",offset:r,node:i}),r=e(i,r),h(i).match(/br|hr|img|input/)||t.push({event:"stop",offset:r,node:i}));return r}(e,0),t}function f(e){return e.variants&&!e.cached_variants&&(e.cached_variants=e.variants.map((function(t){return g(e,{variants:null},t)}))),e.cached_variants?e.cached_variants:function e(t){return!!t&&(t.endsWithParent||e(t.starts))}(e)?[g(e,{starts:e.starts?g(e.starts):null})]:[e]}function b(e,t){return t?Number(t):(o=e,-1!=p.indexOf(o.toLowerCase())?0:1);var o}function y(e){function t(e){return e&&e.source||e}function r(o,r){return new RegExp(t(o),"m"+(e.case_insensitive?"i":"")+(r?"g":""))}function i(e){var o,i,n={},s=[],a={},l=1;function c(e,t){n[l]=e,s.push([e,t]),l+=function(e){return new RegExp(e.toString()+"|").exec("").length-1}(t)+1}for(var p=0;p<e.contains.length;p++)c(i=e.contains[p],i.beginKeywords?"\\.?(?:"+i.begin+")\\.?":i.begin);e.terminator_end&&c("end",e.terminator_end),e.illegal&&c("illegal",e.illegal);var d=s.map((function(e){return e[1]}));return o=r(function(e,o){for(var r=/\[(?:[^\\\]]|\\.)*\]|\(\??|\\([1-9][0-9]*)|\\./,i=0,n="",s=0;s<e.length;s++){var a=i+=1,l=t(e[s]);for(s>0&&(n+=o),n+="(";l.length>0;){var c=r.exec(l);if(null==c){n+=l;break}n+=l.substring(0,c.index),l=l.substring(c.index+c[0].length),"\\"==c[0][0]&&c[1]?n+="\\"+String(Number(c[1])+a):(n+=c[0],"("==c[0]&&i++)}n+=")"}return n}(d,"|"),!0),a.lastIndex=0,a.exec=function(t){var r;if(0===s.length)return null;o.lastIndex=a.lastIndex;var i=o.exec(t);if(!i)return null;for(var l=0;l<i.length;l++)if(null!=i[l]&&null!=n[""+l]){r=n[""+l];break}return"string"==typeof r?(i.type=r,i.extra=[e.illegal,e.terminator_end]):(i.type="begin",i.rule=r),i},a}!function n(s,a){s.compiled||(s.compiled=!0,s.keywords=s.keywords||s.beginKeywords,s.keywords&&(s.keywords=function(e,t){var r={};return"string"==typeof e?i("keyword",e):o(e).forEach((function(t){i(t,e[t])})),r;function i(e,o){t&&(o=o.toLowerCase()),o.split(" ").forEach((function(t){var o=t.split("|");r[o[0]]=[e,b(o[0],o[1])]}))}}(s.keywords,e.case_insensitive)),s.lexemesRe=r(s.lexemes||/\w+/,!0),a&&(s.beginKeywords&&(s.begin="\\b("+s.beginKeywords.split(" ").join("|")+")\\b"),s.begin||(s.begin=/\B|\b/),s.beginRe=r(s.begin),s.endSameAsBegin&&(s.end=s.begin),s.end||s.endsWithParent||(s.end=/\B|\b/),s.end&&(s.endRe=r(s.end)),s.terminator_end=t(s.end)||"",s.endsWithParent&&a.terminator_end&&(s.terminator_end+=(s.end?"|":"")+a.terminator_end)),s.illegal&&(s.illegalRe=r(s.illegal)),null==s.relevance&&(s.relevance=1),s.contains||(s.contains=[]),s.contains=Array.prototype.concat.apply([],s.contains.map((function(e){return f("self"===e?s:e)}))),s.contains.forEach((function(e){n(e,s)})),s.starts&&n(s.starts,a),s.terminators=i(s))}(e)}function v(e,t,o,i){function n(e,t){var o=f.case_insensitive?t[0].toLowerCase():t[0];return e.keywords.hasOwnProperty(o)&&e.keywords[o]}function s(e,t,o,r){if(!o&&""===t)return"";if(!e)return t;var i='<span class="'+(r?"":c.classPrefix);return(i+=e+'">')+t+(o?"":l)}function a(){_+=null!=k.subLanguage?function(){var e="string"==typeof k.subLanguage;if(e&&!r[k.subLanguage])return d(S);var t=e?v(k.subLanguage,S,!0,x[k.subLanguage]):w(S,k.subLanguage.length?k.subLanguage:void 0);return k.relevance>0&&($+=t.relevance),e&&(x[k.subLanguage]=t.top),s(t.language,t.value,!1,!0)}():function(){var e,t,o,r;if(!k.keywords)return d(S);for(r="",t=0,k.lexemesRe.lastIndex=0,o=k.lexemesRe.exec(S);o;)r+=d(S.substring(t,o.index)),(e=n(k,o))?($+=e[1],r+=s(e[0],d(o[0]))):r+=d(o[0]),t=k.lexemesRe.lastIndex,o=k.lexemesRe.exec(S);return r+d(S.substr(t))}(),S=""}function p(e){_+=e.className?s(e.className,"",!0):"",k=Object.create(e,{parent:{value:k}})}function h(e){var t=e[0],o=e.rule;return o&&o.endSameAsBegin&&(o.endRe=function(e){return new RegExp(e.replace(/[-\/\\^$*+?.()|[\]{}]/g,"\\$&"),"m")}(t)),o.skip?S+=t:(o.excludeBegin&&(S+=t),a(),o.returnBegin||o.excludeBegin||(S=t)),p(o),o.returnBegin?0:t.length}function u(e){var t=e[0],o=function e(t,o){if(function(e,t){var o=e&&e.exec(t);return o&&0===o.index}(t.endRe,o)){for(;t.endsParent&&t.parent;)t=t.parent;return t}if(t.endsWithParent)return e(t.parent,o)}(k,t);if(o){var r=k;r.skip?S+=t:(r.returnEnd||r.excludeEnd||(S+=t),a(),r.excludeEnd&&(S=t));do{k.className&&(_+=l),k.skip||k.subLanguage||($+=k.relevance),k=k.parent}while(k!==o.parent);return o.starts&&(o.endSameAsBegin&&(o.starts.endRe=o.endRe),p(o.starts)),r.returnEnd?0:t.length}}var g={};function m(e,r){var i=r&&r[0];if(S+=e,null==i)return a(),0;if("begin"==g.type&&"end"==r.type&&g.index==r.index&&""===i)return S+=t.slice(r.index,r.index+1),1;if(g=r,"begin"===r.type)return h(r);if("illegal"===r.type&&!o)throw new Error('Illegal lexeme "'+i+'" for mode "'+(k.className||"<unnamed>")+'"');if("end"===r.type){var n=u(r);if(null!=n)return n}return S+=i,i.length}var f=A(e);if(!f)throw new Error('Unknown language: "'+e+'"');y(f);var b,k=i||f,x={},_="";for(b=k;b!==f;b=b.parent)b.className&&(_=s(b.className,"",!0)+_);var S="",$=0;try{for(var E,z,C=0;k.terminators.lastIndex=C,E=k.terminators.exec(t);)z=m(t.substring(C,E.index),E),C=E.index+z;for(m(t.substr(C)),b=k;b.parent;b=b.parent)b.className&&(_+=l);return{relevance:$,value:_,illegal:!1,language:e,top:k}}catch(e){if(e.message&&-1!==e.message.indexOf("Illegal"))return{illegal:!0,relevance:0,value:d(t)};throw e}}function w(e,t){t=t||c.languages||o(r);var i={relevance:0,value:d(e)},n=i;return t.filter(A).filter(S).forEach((function(t){var o=v(t,e,!1);o.language=t,o.relevance>n.relevance&&(n=o),o.relevance>i.relevance&&(n=i,i=o)})),n.language&&(i.second_best=n),i}function k(e){return c.tabReplace||c.useBR?e.replace(a,(function(e,t){return c.useBR&&"\n"===e?"<br>":c.tabReplace?t.replace(/\t/g,c.tabReplace):""})):e}function x(e){var o,r,n,a,l,p=function(e){var t,o,r,i,n=e.className+" ";if(n+=e.parentNode?e.parentNode.className:"",o=s.exec(n))return A(o[1])?o[1]:"no-highlight";for(t=0,r=(n=n.split(/\s+/)).length;t<r;t++)if(u(i=n[t])||A(i))return i}(e);u(p)||(c.useBR?(o=document.createElementNS("http://www.w3.org/1999/xhtml","div")).innerHTML=e.innerHTML.replace(/\n/g,"").replace(/<br[ \/]*>/g,"\n"):o=e,l=o.textContent,n=p?v(p,l,!0):w(l),(r=m(o)).length&&((a=document.createElementNS("http://www.w3.org/1999/xhtml","div")).innerHTML=n.value,n.value=function(e,o,r){var i=0,n="",s=[];function a(){return e.length&&o.length?e[0].offset!==o[0].offset?e[0].offset<o[0].offset?e:o:"start"===o[0].event?e:o:e.length?e:o}function l(e){n+="<"+h(e)+t.map.call(e.attributes,(function(e){return" "+e.nodeName+'="'+d(e.value).replace('"',"&quot;")+'"'})).join("")+">"}function c(e){n+="</"+h(e)+">"}function p(e){("start"===e.event?l:c)(e.node)}for(;e.length||o.length;){var u=a();if(n+=d(r.substring(i,u[0].offset)),i=u[0].offset,u===e){s.reverse().forEach(c);do{p(u.splice(0,1)[0]),u=a()}while(u===e&&u.length&&u[0].offset===i);s.reverse().forEach(l)}else"start"===u[0].event?s.push(u[0].node):s.pop(),p(u.splice(0,1)[0])}return n+d(r.substr(i))}(r,m(a),l)),n.value=k(n.value),e.innerHTML=n.value,e.className=function(e,t,o){var r=t?i[t]:o,n=[e.trim()];return e.match(/\bhljs\b/)||n.push("hljs"),-1===e.indexOf(r)&&n.push(r),n.join(" ").trim()}(e.className,p,n.language),e.result={language:n.language,re:n.relevance},n.second_best&&(e.second_best={language:n.second_best.language,re:n.second_best.relevance}))}function _(){if(!_.called){_.called=!0;var e=document.querySelectorAll("pre code");t.forEach.call(e,x)}}function A(e){return e=(e||"").toLowerCase(),r[e]||r[i[e]]}function S(e){var t=A(e);return t&&!t.disableAutodetect}return e.highlight=v,e.highlightAuto=w,e.fixMarkup=k,e.highlightBlock=x,e.configure=function(e){c=g(c,e)},e.initHighlighting=_,e.initHighlightingOnLoad=function(){addEventListener("DOMContentLoaded",_,!1),addEventListener("load",_,!1)},e.registerLanguage=function(t,o){var n=r[t]=o(e);n.rawDefinition=o.bind(null,e),n.aliases&&n.aliases.forEach((function(e){i[e]=t}))},e.listLanguages=function(){return o(r)},e.getLanguage=A,e.autoDetection=S,e.inherit=g,e.IDENT_RE="[a-zA-Z]\\w*",e.UNDERSCORE_IDENT_RE="[a-zA-Z_]\\w*",e.NUMBER_RE="\\b\\d+(\\.\\d+)?",e.C_NUMBER_RE="(-?)(\\b0[xX][a-fA-F0-9]+|(\\b\\d+(\\.\\d*)?|\\.\\d+)([eE][-+]?\\d+)?)",e.BINARY_NUMBER_RE="\\b(0b[01]+)",e.RE_STARTERS_RE="!|!=|!==|%|%=|&|&&|&=|\\*|\\*=|\\+|\\+=|,|-|-=|/=|/|:|;|<<|<<=|<=|<|===|==|=|>>>=|>>=|>=|>>>|>>|>|\\?|\\[|\\{|\\(|\\^|\\^=|\\||\\|=|\\|\\||~",e.BACKSLASH_ESCAPE={begin:"\\\\[\\s\\S]",relevance:0},e.APOS_STRING_MODE={className:"string",begin:"'",end:"'",illegal:"\\n",contains:[e.BACKSLASH_ESCAPE]},e.QUOTE_STRING_MODE={className:"string",begin:'"',end:'"',illegal:"\\n",contains:[e.BACKSLASH_ESCAPE]},e.PHRASAL_WORDS_MODE={begin:/\b(a|an|the|are|I'm|isn't|don't|doesn't|won't|but|just|should|pretty|simply|enough|gonna|going|wtf|so|such|will|you|your|they|like|more)\b/},e.COMMENT=function(t,o,r){var i=e.inherit({className:"comment",begin:t,end:o,contains:[]},r||{});return i.contains.push(e.PHRASAL_WORDS_MODE),i.contains.push({className:"doctag",begin:"(?:TODO|FIXME|NOTE|BUG|XXX):",relevance:0}),i},e.C_LINE_COMMENT_MODE=e.COMMENT("//","$"),e.C_BLOCK_COMMENT_MODE=e.COMMENT("/\\*","\\*/"),e.HASH_COMMENT_MODE=e.COMMENT("#","$"),e.NUMBER_MODE={className:"number",begin:e.NUMBER_RE,relevance:0},e.C_NUMBER_MODE={className:"number",begin:e.C_NUMBER_RE,relevance:0},e.BINARY_NUMBER_MODE={className:"number",begin:e.BINARY_NUMBER_RE,relevance:0},e.CSS_NUMBER_MODE={className:"number",begin:e.NUMBER_RE+"(%|em|ex|ch|rem|vw|vh|vmin|vmax|cm|mm|in|pt|pc|px|deg|grad|rad|turn|s|ms|Hz|kHz|dpi|dpcm|dppx)?",relevance:0},e.REGEXP_MODE={className:"regexp",begin:/\//,end:/\/[gimuy]*/,illegal:/\n/,contains:[e.BACKSLASH_ESCAPE,{begin:/\[/,end:/\]/,relevance:0,contains:[e.BACKSLASH_ESCAPE]}]},e.TITLE_MODE={className:"title",begin:e.IDENT_RE,relevance:0},e.UNDERSCORE_TITLE_MODE={className:"title",begin:e.UNDERSCORE_IDENT_RE,relevance:0},e.METHOD_GUARD={begin:"\\.\\s*"+e.UNDERSCORE_IDENT_RE,relevance:0},e},r="object"==typeof window&&window||"object"==typeof self&&self,t.nodeType?r&&(r.hljs=o({})):o(t)})));const vt=ce`
  /*

github.com style (c) Vasily Polovnyov <vast@whiteants.net>

*/

  .hljs {
    display: block;
    overflow-x: auto;
    padding: 0.5em;
    color: #333;
    background: #f8f8f8;
  }

  .hljs-comment,
  .hljs-quote {
    color: #998;
    font-style: italic;
  }

  .hljs-keyword,
  .hljs-selector-tag,
  .hljs-subst {
    color: #333;
    font-weight: bold;
  }

  .hljs-number,
  .hljs-literal,
  .hljs-variable,
  .hljs-template-variable,
  .hljs-tag .hljs-attr {
    color: #008080;
  }

  .hljs-string,
  .hljs-doctag {
    color: #d14;
  }

  .hljs-title,
  .hljs-section,
  .hljs-selector-id {
    color: #900;
    font-weight: bold;
  }

  .hljs-subst {
    font-weight: normal;
  }

  .hljs-type,
  .hljs-class .hljs-title {
    color: #458;
    font-weight: bold;
  }

  .hljs-tag,
  .hljs-name,
  .hljs-attribute {
    color: #000080;
    font-weight: normal;
  }

  .hljs-regexp,
  .hljs-link {
    color: #009926;
  }

  .hljs-symbol,
  .hljs-bullet {
    color: #990073;
  }

  .hljs-built_in,
  .hljs-builtin-name {
    color: #0086b3;
  }

  .hljs-meta {
    color: #999;
    font-weight: bold;
  }

  .hljs-deletion {
    background: #fdd;
  }

  .hljs-addition {
    background: #dfd;
  }

  .hljs-emphasis {
    font-style: italic;
  }

  .hljs-strong {
    font-weight: bold;
  }
`,wt=[ce`
  @font-face {
    font-family: octicons-link;
    src: url(data:font/woff;charset=utf-8;base64,d09GRgABAAAAAAZwABAAAAAACFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEU0lHAAAGaAAAAAgAAAAIAAAAAUdTVUIAAAZcAAAACgAAAAoAAQAAT1MvMgAAAyQAAABJAAAAYFYEU3RjbWFwAAADcAAAAEUAAACAAJThvmN2dCAAAATkAAAABAAAAAQAAAAAZnBnbQAAA7gAAACyAAABCUM+8IhnYXNwAAAGTAAAABAAAAAQABoAI2dseWYAAAFsAAABPAAAAZwcEq9taGVhZAAAAsgAAAA0AAAANgh4a91oaGVhAAADCAAAABoAAAAkCA8DRGhtdHgAAAL8AAAADAAAAAwGAACfbG9jYQAAAsAAAAAIAAAACABiATBtYXhwAAACqAAAABgAAAAgAA8ASm5hbWUAAAToAAABQgAAAlXu73sOcG9zdAAABiwAAAAeAAAAME3QpOBwcmVwAAAEbAAAAHYAAAB/aFGpk3jaTY6xa8JAGMW/O62BDi0tJLYQincXEypYIiGJjSgHniQ6umTsUEyLm5BV6NDBP8Tpts6F0v+k/0an2i+itHDw3v2+9+DBKTzsJNnWJNTgHEy4BgG3EMI9DCEDOGEXzDADU5hBKMIgNPZqoD3SilVaXZCER3/I7AtxEJLtzzuZfI+VVkprxTlXShWKb3TBecG11rwoNlmmn1P2WYcJczl32etSpKnziC7lQyWe1smVPy/Lt7Kc+0vWY/gAgIIEqAN9we0pwKXreiMasxvabDQMM4riO+qxM2ogwDGOZTXxwxDiycQIcoYFBLj5K3EIaSctAq2kTYiw+ymhce7vwM9jSqO8JyVd5RH9gyTt2+J/yUmYlIR0s04n6+7Vm1ozezUeLEaUjhaDSuXHwVRgvLJn1tQ7xiuVv/ocTRF42mNgZGBgYGbwZOBiAAFGJBIMAAizAFoAAABiAGIAznjaY2BkYGAA4in8zwXi+W2+MjCzMIDApSwvXzC97Z4Ig8N/BxYGZgcgl52BCSQKAA3jCV8CAABfAAAAAAQAAEB42mNgZGBg4f3vACQZQABIMjKgAmYAKEgBXgAAeNpjYGY6wTiBgZWBg2kmUxoDA4MPhGZMYzBi1AHygVLYQUCaawqDA4PChxhmh/8ODDEsvAwHgMKMIDnGL0x7gJQCAwMAJd4MFwAAAHjaY2BgYGaA4DAGRgYQkAHyGMF8NgYrIM3JIAGVYYDT+AEjAwuDFpBmA9KMDEwMCh9i/v8H8sH0/4dQc1iAmAkALaUKLgAAAHjaTY9LDsIgEIbtgqHUPpDi3gPoBVyRTmTddOmqTXThEXqrob2gQ1FjwpDvfwCBdmdXC5AVKFu3e5MfNFJ29KTQT48Ob9/lqYwOGZxeUelN2U2R6+cArgtCJpauW7UQBqnFkUsjAY/kOU1cP+DAgvxwn1chZDwUbd6CFimGXwzwF6tPbFIcjEl+vvmM/byA48e6tWrKArm4ZJlCbdsrxksL1AwWn/yBSJKpYbq8AXaaTb8AAHja28jAwOC00ZrBeQNDQOWO//sdBBgYGRiYWYAEELEwMTE4uzo5Zzo5b2BxdnFOcALxNjA6b2ByTswC8jYwg0VlNuoCTWAMqNzMzsoK1rEhNqByEyerg5PMJlYuVueETKcd/89uBpnpvIEVomeHLoMsAAe1Id4AAAAAAAB42oWQT07CQBTGv0JBhagk7HQzKxca2sJCE1hDt4QF+9JOS0nbaaYDCQfwCJ7Au3AHj+LO13FMmm6cl7785vven0kBjHCBhfpYuNa5Ph1c0e2Xu3jEvWG7UdPDLZ4N92nOm+EBXuAbHmIMSRMs+4aUEd4Nd3CHD8NdvOLTsA2GL8M9PODbcL+hD7C1xoaHeLJSEao0FEW14ckxC+TU8TxvsY6X0eLPmRhry2WVioLpkrbp84LLQPGI7c6sOiUzpWIWS5GzlSgUzzLBSikOPFTOXqly7rqx0Z1Q5BAIoZBSFihQYQOOBEdkCOgXTOHA07HAGjGWiIjaPZNW13/+lm6S9FT7rLHFJ6fQbkATOG1j2OFMucKJJsxIVfQORl+9Jyda6Sl1dUYhSCm1dyClfoeDve4qMYdLEbfqHf3O/AdDumsjAAB42mNgYoAAZQYjBmyAGYQZmdhL8zLdDEydARfoAqIAAAABAAMABwAKABMAB///AA8AAQAAAAAAAAAAAAAAAAABAAAAAA==)
      format('woff');
  }
`,ce`
  .markdown-body .octicon {
    display: inline-block;
    fill: currentColor;
    vertical-align: text-bottom;
  }

  .markdown-body .anchor {
    float: left;
    line-height: 1;
    margin-left: -20px;
    padding-right: 4px;
  }

  .markdown-body .anchor:focus {
    outline: none;
  }

  .markdown-body h1 .octicon-link,
  .markdown-body h2 .octicon-link,
  .markdown-body h3 .octicon-link,
  .markdown-body h4 .octicon-link,
  .markdown-body h5 .octicon-link,
  .markdown-body h6 .octicon-link {
    color: #1b1f23;
    vertical-align: middle;
    visibility: hidden;
  }

  .markdown-body h1:hover .anchor,
  .markdown-body h2:hover .anchor,
  .markdown-body h3:hover .anchor,
  .markdown-body h4:hover .anchor,
  .markdown-body h5:hover .anchor,
  .markdown-body h6:hover .anchor {
    text-decoration: none;
  }

  .markdown-body h1:hover .anchor .octicon-link,
  .markdown-body h2:hover .anchor .octicon-link,
  .markdown-body h3:hover .anchor .octicon-link,
  .markdown-body h4:hover .anchor .octicon-link,
  .markdown-body h5:hover .anchor .octicon-link,
  .markdown-body h6:hover .anchor .octicon-link {
    visibility: visible;
  }
  .markdown-body {
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    line-height: 1.5;
    color: #24292e;
    font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji,
      Segoe UI Emoji;
    font-size: 16px;
    line-height: 1.5;
    word-wrap: break-word;
  }

  .markdown-body .pl-c {
    color: #6a737d;
  }

  .markdown-body .pl-c1,
  .markdown-body .pl-s .pl-v {
    color: #005cc5;
  }

  .markdown-body .pl-e,
  .markdown-body .pl-en {
    color: #6f42c1;
  }

  .markdown-body .pl-s .pl-s1,
  .markdown-body .pl-smi {
    color: #24292e;
  }

  .markdown-body .pl-ent {
    color: #22863a;
  }

  .markdown-body .pl-k {
    color: #d73a49;
  }

  .markdown-body .pl-pds,
  .markdown-body .pl-s,
  .markdown-body .pl-s .pl-pse .pl-s1,
  .markdown-body .pl-sr,
  .markdown-body .pl-sr .pl-cce,
  .markdown-body .pl-sr .pl-sra,
  .markdown-body .pl-sr .pl-sre {
    color: #032f62;
  }

  .markdown-body .pl-smw,
  .markdown-body .pl-v {
    color: #e36209;
  }

  .markdown-body .pl-bu {
    color: #b31d28;
  }

  .markdown-body .pl-ii {
    color: #fafbfc;
    background-color: #b31d28;
  }

  .markdown-body .pl-c2 {
    color: #fafbfc;
    background-color: #d73a49;
  }

  .markdown-body .pl-c2:before {
    content: '^M';
  }

  .markdown-body .pl-sr .pl-cce {
    font-weight: 700;
    color: #22863a;
  }

  .markdown-body .pl-ml {
    color: #735c0f;
  }

  .markdown-body .pl-mh,
  .markdown-body .pl-mh .pl-en,
  .markdown-body .pl-ms {
    font-weight: 700;
    color: #005cc5;
  }

  .markdown-body .pl-mi {
    font-style: italic;
    color: #24292e;
  }

  .markdown-body .pl-mb {
    font-weight: 700;
    color: #24292e;
  }

  .markdown-body .pl-md {
    color: #b31d28;
    background-color: #ffeef0;
  }

  .markdown-body .pl-mi1 {
    color: #22863a;
    background-color: #f0fff4;
  }

  .markdown-body .pl-mc {
    color: #e36209;
    background-color: #ffebda;
  }

  .markdown-body .pl-mi2 {
    color: #f6f8fa;
    background-color: #005cc5;
  }

  .markdown-body .pl-mdr {
    font-weight: 700;
    color: #6f42c1;
  }

  .markdown-body .pl-ba {
    color: #586069;
  }

  .markdown-body .pl-sg {
    color: #959da5;
  }

  .markdown-body .pl-corl {
    text-decoration: underline;
    color: #032f62;
  }

  .markdown-body details {
    display: block;
  }

  .markdown-body summary {
    display: list-item;
  }

  .markdown-body a {
    background-color: initial;
  }

  .markdown-body a:active,
  .markdown-body a:hover {
    outline-width: 0;
  }

  .markdown-body strong {
    font-weight: inherit;
    font-weight: bolder;
  }

  .markdown-body h1 {
    font-size: 2em;
    margin: 0.67em 0;
  }

  .markdown-body img {
    border-style: none;
  }

  .markdown-body code,
  .markdown-body kbd,
  .markdown-body pre {
    font-family: monospace, monospace;
    font-size: 1em;
  }

  .markdown-body hr {
    box-sizing: initial;
    height: 0;
    overflow: visible;
  }

  .markdown-body input {
    font: inherit;
    margin: 0;
  }

  .markdown-body input {
    overflow: visible;
  }

  .markdown-body [type='checkbox'] {
    box-sizing: border-box;
    padding: 0;
  }

  .markdown-body * {
    box-sizing: border-box;
  }

  .markdown-body input {
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
  }

  .markdown-body a {
    color: #0366d6;
    text-decoration: none;
  }

  .markdown-body a:hover {
    text-decoration: underline;
  }

  .markdown-body strong {
    font-weight: 600;
  }

  .markdown-body hr {
    height: 0;
    margin: 15px 0;
    overflow: hidden;
    background: transparent;
    border: 0;
    border-bottom: 1px solid #dfe2e5;
  }

  .markdown-body hr:after,
  .markdown-body hr:before {
    display: table;
    content: '';
  }

  .markdown-body hr:after {
    clear: both;
  }

  .markdown-body table {
    border-spacing: 0;
    border-collapse: collapse;
  }

  .markdown-body td,
  .markdown-body th {
    padding: 0;
  }

  .markdown-body details summary {
    cursor: pointer;
  }

  .markdown-body kbd {
    display: inline-block;
    padding: 3px 5px;
    font: 11px SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
    line-height: 10px;
    color: #444d56;
    vertical-align: middle;
    background-color: #fafbfc;
    border: 1px solid #d1d5da;
    border-radius: 3px;
    box-shadow: inset 0 -1px 0 #d1d5da;
  }

  .markdown-body h1,
  .markdown-body h2,
  .markdown-body h3,
  .markdown-body h4,
  .markdown-body h5,
  .markdown-body h6 {
    margin-top: 0;
    margin-bottom: 0;
  }

  .markdown-body h1 {
    font-size: 32px;
  }

  .markdown-body h1,
  .markdown-body h2 {
    font-weight: 600;
  }

  .markdown-body h2 {
    font-size: 24px;
  }

  .markdown-body h3 {
    font-size: 20px;
  }

  .markdown-body h3,
  .markdown-body h4 {
    font-weight: 600;
  }

  .markdown-body h4 {
    font-size: 16px;
  }

  .markdown-body h5 {
    font-size: 14px;
  }

  .markdown-body h5,
  .markdown-body h6 {
    font-weight: 600;
  }

  .markdown-body h6 {
    font-size: 12px;
  }

  .markdown-body p {
    margin-top: 0;
    margin-bottom: 10px;
  }

  .markdown-body blockquote {
    margin: 0;
  }

  .markdown-body ol,
  .markdown-body ul {
    padding-left: 0;
    margin-top: 0;
    margin-bottom: 0;
  }

  .markdown-body ol ol,
  .markdown-body ul ol {
    list-style-type: lower-roman;
  }

  .markdown-body ol ol ol,
  .markdown-body ol ul ol,
  .markdown-body ul ol ol,
  .markdown-body ul ul ol {
    list-style-type: lower-alpha;
  }

  .markdown-body dd {
    margin-left: 0;
  }

  .markdown-body code,
  .markdown-body pre {
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
    font-size: 12px;
  }

  .markdown-body pre {
    margin-top: 0;
    margin-bottom: 0;
  }

  .markdown-body input::-webkit-inner-spin-button,
  .markdown-body input::-webkit-outer-spin-button {
    margin: 0;
    -webkit-appearance: none;
    appearance: none;
  }

  .markdown-body .border {
    border: 1px solid #e1e4e8 !important;
  }

  .markdown-body .border-0 {
    border: 0 !important;
  }

  .markdown-body .border-bottom {
    border-bottom: 1px solid #e1e4e8 !important;
  }

  .markdown-body .rounded-1 {
    border-radius: 3px !important;
  }

  .markdown-body .bg-white {
    background-color: #fff !important;
  }

  .markdown-body .bg-gray-light {
    background-color: #fafbfc !important;
  }

  .markdown-body .text-gray-light {
    color: #6a737d !important;
  }

  .markdown-body .mb-0 {
    margin-bottom: 0 !important;
  }

  .markdown-body .my-2 {
    margin-top: 8px !important;
    margin-bottom: 8px !important;
  }

  .markdown-body .pl-0 {
    padding-left: 0 !important;
  }

  .markdown-body .py-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .markdown-body .pl-1 {
    padding-left: 4px !important;
  }

  .markdown-body .pl-2 {
    padding-left: 8px !important;
  }

  .markdown-body .py-2 {
    padding-top: 8px !important;
    padding-bottom: 8px !important;
  }

  .markdown-body .pl-3,
  .markdown-body .px-3 {
    padding-left: 16px !important;
  }

  .markdown-body .px-3 {
    padding-right: 16px !important;
  }

  .markdown-body .pl-4 {
    padding-left: 24px !important;
  }

  .markdown-body .pl-5 {
    padding-left: 32px !important;
  }

  .markdown-body .pl-6 {
    padding-left: 40px !important;
  }

  .markdown-body .f6 {
    font-size: 12px !important;
  }

  .markdown-body .lh-condensed {
    line-height: 1.25 !important;
  }

  .markdown-body .text-bold {
    font-weight: 600 !important;
  }

  .markdown-body .pl-7 {
    padding-left: 48px !important;
  }

  .markdown-body .pl-8 {
    padding-left: 64px !important;
  }

  .markdown-body .pl-9 {
    padding-left: 80px !important;
  }

  .markdown-body .pl-10 {
    padding-left: 96px !important;
  }

  .markdown-body .pl-11 {
    padding-left: 112px !important;
  }

  .markdown-body .pl-12 {
    padding-left: 128px !important;
  }

  .markdown-body hr {
    border-bottom-color: #eee;
  }

  .markdown-body kbd {
    display: inline-block;
    padding: 3px 5px;
    font: 11px SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
    line-height: 10px;
    color: #444d56;
    vertical-align: middle;
    background-color: #fafbfc;
    border: 1px solid #d1d5da;
    border-radius: 3px;
    box-shadow: inset 0 -1px 0 #d1d5da;
  }

  .markdown-body:after,
  .markdown-body:before {
    display: table;
    content: '';
  }

  .markdown-body:after {
    clear: both;
  }

  .markdown-body > :first-child {
    margin-top: 0 !important;
  }

  .markdown-body > :last-child {
    margin-bottom: 0 !important;
  }

  .markdown-body a:not([href]) {
    color: inherit;
    text-decoration: none;
  }
`,ce`
  .markdown-body blockquote,
  .markdown-body details,
  .markdown-body dl,
  .markdown-body ol,
  .markdown-body p,
  .markdown-body pre,
  .markdown-body table,
  .markdown-body ul {
    margin-top: 0;
    margin-bottom: 16px;
  }

  .markdown-body hr {
    height: 0.25em;
    padding: 0;
    margin: 24px 0;
    background-color: #e1e4e8;
    border: 0;
  }

  .markdown-body blockquote {
    padding: 0 1em;
    color: #6a737d;
    border-left: 0.25em solid #dfe2e5;
  }

  .markdown-body blockquote > :first-child {
    margin-top: 0;
  }

  .markdown-body blockquote > :last-child {
    margin-bottom: 0;
  }

  .markdown-body h1,
  .markdown-body h2,
  .markdown-body h3,
  .markdown-body h4,
  .markdown-body h5,
  .markdown-body h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
  }

  .markdown-body h1 {
    font-size: 2em;
  }

  .markdown-body h1,
  .markdown-body h2 {
    padding-bottom: 0.3em;
    border-bottom: 1px solid #eaecef;
  }

  .markdown-body h2 {
    font-size: 1.5em;
  }

  .markdown-body h3 {
    font-size: 1.25em;
  }

  .markdown-body h4 {
    font-size: 1em;
  }

  .markdown-body h5 {
    font-size: 0.875em;
  }

  .markdown-body h6 {
    font-size: 0.85em;
    color: #6a737d;
  }

  .markdown-body ol,
  .markdown-body ul {
    padding-left: 2em;
  }

  .markdown-body ol ol,
  .markdown-body ol ul,
  .markdown-body ul ol,
  .markdown-body ul ul {
    margin-top: 0;
    margin-bottom: 0;
  }

  .markdown-body li {
    word-wrap: break-all;
  }

  .markdown-body li > p {
    margin-top: 16px;
  }

  .markdown-body li + li {
    margin-top: 0.25em;
  }

  .markdown-body dl {
    padding: 0;
  }

  .markdown-body dl dt {
    padding: 0;
    margin-top: 16px;
    font-size: 1em;
    font-style: italic;
    font-weight: 600;
  }

  .markdown-body dl dd {
    padding: 0 16px;
    margin-bottom: 16px;
  }

  .markdown-body table {
    display: block;
    width: 100%;
    overflow: auto;
  }

  .markdown-body table th {
    font-weight: 600;
  }

  .markdown-body table td,
  .markdown-body table th {
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
  }

  .markdown-body table tr {
    background-color: #fff;
    border-top: 1px solid #c6cbd1;
  }

  .markdown-body table tr:nth-child(2n) {
    background-color: #f6f8fa;
  }

  .markdown-body img {
    max-width: 100%;
    box-sizing: initial;
    background-color: #fff;
  }

  .markdown-body img[align='right'] {
    padding-left: 20px;
  }

  .markdown-body img[align='left'] {
    padding-right: 20px;
  }

  .markdown-body code {
    padding: 0.2em 0.4em;
    margin: 0;
    font-size: 85%;
    background-color: rgba(27, 31, 35, 0.05);
    border-radius: 3px;
  }

  .markdown-body pre {
    word-wrap: normal;
  }

  .markdown-body pre > code {
    padding: 0;
    margin: 0;
    font-size: 100%;
    word-break: normal;
    white-space: pre;
    background: transparent;
    border: 0;
  }

  .markdown-body .highlight {
    margin-bottom: 16px;
  }

  .markdown-body .highlight pre {
    margin-bottom: 0;
    word-break: normal;
  }

  .markdown-body .highlight pre,
  .markdown-body pre {
    padding: 16px;
    overflow: auto;
    font-size: 85%;
    line-height: 1.45;
    background-color: #f6f8fa;
    border-radius: 3px;
  }

  .markdown-body pre code {
    display: inline;
    max-width: auto;
    padding: 0;
    margin: 0;
    overflow: visible;
    line-height: inherit;
    word-wrap: normal;
    background-color: initial;
    border: 0;
  }

  .markdown-body .commit-tease-sha {
    display: inline-block;
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
    font-size: 90%;
    color: #444d56;
  }

  .markdown-body .full-commit .btn-outline:not(:disabled):hover {
    color: #005cc5;
    border-color: #005cc5;
  }

  .markdown-body .blob-wrapper {
    overflow-x: auto;
    overflow-y: hidden;
  }

  .markdown-body .blob-wrapper-embedded {
    max-height: 240px;
    overflow-y: auto;
  }

  .markdown-body .blob-num {
    width: 1%;
    min-width: 50px;
    padding-right: 10px;
    padding-left: 10px;
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
    font-size: 12px;
    line-height: 20px;
    color: rgba(27, 31, 35, 0.3);
    text-align: right;
    white-space: nowrap;
    vertical-align: top;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  .markdown-body .blob-num:hover {
    color: rgba(27, 31, 35, 0.6);
  }

  .markdown-body .blob-num:before {
    content: attr(data-line-number);
  }

  .markdown-body .blob-code {
    position: relative;
    padding-right: 10px;
    padding-left: 10px;
    line-height: 20px;
    vertical-align: top;
  }

  .markdown-body .blob-code-inner {
    overflow: visible;
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
    font-size: 12px;
    color: #24292e;
    word-wrap: normal;
    white-space: pre;
  }

  .markdown-body .pl-token.active,
  .markdown-body .pl-token:hover {
    cursor: pointer;
    background: #ffea7f;
  }

  .markdown-body :checked + .radio-label {
    position: relative;
    z-index: 1;
    border-color: #0366d6;
  }

  .markdown-body .select-menu-item input[type='radio']:not(:checked) + .octicon-check,
  .markdown-body .select-menu-item input[type='radio']:not(:checked) + .octicon-circle-slash {
    visibility: hidden;
  }

  .markdown-body .pl-7 {
    padding-left: 48px !important;
  }

  .markdown-body .pl-8 {
    padding-left: 64px !important;
  }

  .markdown-body .pl-9 {
    padding-left: 80px !important;
  }

  .markdown-body .pl-10 {
    padding-left: 96px !important;
  }

  .markdown-body .pl-11 {
    padding-left: 112px !important;
  }

  .markdown-body .pl-12 {
    padding-left: 128px !important;
  }

  .markdown-body .tab-size[data-tab-size='1'] {
    -moz-tab-size: 1;
    tab-size: 1;
  }

  .markdown-body .tab-size[data-tab-size='2'] {
    -moz-tab-size: 2;
    tab-size: 2;
  }

  .markdown-body .tab-size[data-tab-size='3'] {
    -moz-tab-size: 3;
    tab-size: 3;
  }

  .markdown-body .tab-size[data-tab-size='4'] {
    -moz-tab-size: 4;
    tab-size: 4;
  }

  .markdown-body .tab-size[data-tab-size='5'] {
    -moz-tab-size: 5;
    tab-size: 5;
  }

  .markdown-body .tab-size[data-tab-size='6'] {
    -moz-tab-size: 6;
    tab-size: 6;
  }

  .markdown-body .tab-size[data-tab-size='7'] {
    -moz-tab-size: 7;
    tab-size: 7;
  }

  .markdown-body .tab-size[data-tab-size='8'] {
    -moz-tab-size: 8;
    tab-size: 8;
  }

  .markdown-body .tab-size[data-tab-size='9'] {
    -moz-tab-size: 9;
    tab-size: 9;
  }

  .markdown-body .tab-size[data-tab-size='10'] {
    -moz-tab-size: 10;
    tab-size: 10;
  }

  .markdown-body .tab-size[data-tab-size='11'] {
    -moz-tab-size: 11;
    tab-size: 11;
  }

  .markdown-body .tab-size[data-tab-size='12'] {
    -moz-tab-size: 12;
    tab-size: 12;
  }

  .markdown-body .task-list-item {
    list-style-type: none;
  }

  .markdown-body .task-list-item + .task-list-item {
    margin-top: 3px;
  }

  .markdown-body .task-list-item input {
    margin: 0 0.2em 0.25em -1.6em;
    vertical-align: middle;
  }
`];yt.registerLanguage("yaml",(function(e){var t={className:"string",relevance:0,variants:[{begin:/'/,end:/'/},{begin:/"/,end:/"/},{begin:/\S+/}],contains:[e.BACKSLASH_ESCAPE,{className:"template-variable",variants:[{begin:"{{",end:"}}"},{begin:"%{",end:"}"}]}]};return{case_insensitive:!0,aliases:["yml","YAML","yaml"],contains:[{className:"attr",variants:[{begin:"\\w[\\w :\\/.-]*:(?=[ \t]|$)"},{begin:'"\\w[\\w :\\/.-]*":(?=[ \t]|$)'},{begin:"'\\w[\\w :\\/.-]*':(?=[ \t]|$)"}]},{className:"meta",begin:"^---s*$",relevance:10},{className:"string",begin:"[\\|>]([0-9]?[+-])?[ ]*\\n( *)[\\S ]+\\n(\\2[\\S ]+\\n?)*"},{begin:"<%[%=-]?",end:"[%-]?%>",subLanguage:"ruby",excludeBegin:!0,excludeEnd:!0,relevance:0},{className:"type",begin:"!"+e.UNDERSCORE_IDENT_RE},{className:"type",begin:"!!"+e.UNDERSCORE_IDENT_RE},{className:"meta",begin:"&"+e.UNDERSCORE_IDENT_RE+"$"},{className:"meta",begin:"\\*"+e.UNDERSCORE_IDENT_RE+"$"},{className:"bullet",begin:"\\-(?=[ ]|$)",relevance:0},e.HASH_COMMENT_MODE,{beginKeywords:"true false yes no null",keywords:{literal:"true false yes no null"}},{className:"number",begin:e.C_NUMBER_RE+"\\b"},t]}}));const kt=yt,xt=xe;xt.setOptions({highlight:function(e,t){return t&&kt.getLanguage(t)?kt.highlight(t,e,!0).value:kt.highlightAuto(e).value},breaks:!0,gfm:!0,tables:!0,langPrefix:""});let _t=class extends de{render(){return"0"===String(this.authors.length)?P``:P`
            <div class="MobileGrid">
                <p><b>${this.hass.localize("component.hacs.repository.authors")}: </b>

                    ${this.authors.map(e=>P`
                        <a href="https://github.com/${e.replace("@","")}"
                                target="_blank" rel='noreferrer'>
                            ${e.replace("@","")}
                        </a>`)}

                </p>
            </div>
            `}static get styles(){return[ge,ce`
            .autors {

            }
        `]}};e([ne()],_t.prototype,"hass",void 0),e([ne()],_t.prototype,"authors",void 0),_t=e([oe("hacs-authors")],_t);let At=class extends de{render(){return P`
        <paper-menu-button no-animations horizontal-align="right" role="group" aria-haspopup="true" vertical-align="top" aria-disabled="false">
        <paper-icon-button icon="hass:dots-vertical" slot="dropdown-trigger" role="button"></paper-icon-button>
            <paper-listbox slot="dropdown-content" role="listbox" tabindex="0">


                <paper-item @click=${this.RepositoryReload}>
                    ${this.hass.localize("component.hacs.repository.update_information")}
                </paper-item>


                ${"version"===this.repository.version_or_commit?P`
                <paper-item @click=${this.RepositoryBeta}>
                    ${this.repository.beta?this.hass.localize("component.hacs.repository.hide_beta"):this.hass.localize("component.hacs.repository.show_beta")}
                </paper-item>`:""}


                ${this.repository.custom||this.repository.installed?"":P`
                <paper-item @click=${this.RepositoryHide}>
                    ${this.hass.localize("component.hacs.repository.hide")}
                </paper-item>`}


                <a href="https://github.com/${this.repository.full_name}" rel='noreferrer' target="_blank">
                <paper-item>
                    <ha-icon class="link-icon" icon="mdi:open-in-new"></ha-icon>
                    ${this.hass.localize("component.hacs.repository.open_issue")}
                </paper-item>
                </a>


                <a href="https://github.com/hacs/default/issues/new?assignees=ludeeus&labels=flag&template=flag.md&title=${this.repository.full_name}" rel='noreferrer' target="_blank">
                <paper-item>
                    <ha-icon class="link-icon" icon="mdi:open-in-new"></ha-icon>
                    ${this.hass.localize("component.hacs.repository.flag_this")}
                </paper-item>
                </a>


            </paper-listbox>
        </paper-menu-button>
        `}static get styles(){return[ge,ce`
        paper-dropdown-menu {
            width: 250px;
            margin-top: -24px;

          }
          paper-menu-button {
            float: right;
            top: -65px;
          }
        `]}RepositoryReload(){we(this.hass,this.repository.id,"set_state","other"),we(this.hass,this.repository.id,"update")}RepositoryBeta(){we(this.hass,this.repository.id,"set_state","other"),this.repository.beta?we(this.hass,this.repository.id,"hide_beta"):we(this.hass,this.repository.id,"show_beta")}RepositoryHide(){we(this.hass,this.repository.id,"set_state","other"),this.repository.hide?we(this.hass,this.repository.id,"unhide"):we(this.hass,this.repository.id,"hide")}};e([ne()],At.prototype,"hass",void 0),e([ne()],At.prototype,"repository",void 0),At=e([oe("hacs-repository-menu")],At);let St=class extends be{render(){if("plugin"!=this.repository.category)return P``;if(!this.repository.installed)return P``;const e=this.repository.local_path.split("/");return P`
            <a href="/community_plugin/${e.pop()}/${this.repository.file_name}" target="_blank">
                <mwc-button>
                    ${this.hass.localize("component.hacs.repository.open_plugin")}
                </mwc-button>
            </a>
        `}};St=e([oe("hacs-button-open-plugin")],St);let $t=class extends be{render(){return P`
            <a href="https://github.com/${this.repository.full_name}" rel='noreferrer' target="_blank">
                <mwc-button>
                    ${this.hass.localize("component.hacs.repository.repository")}
                </mwc-button>
            </a>
        `}};$t=e([oe("hacs-button-open-repository")],$t);let Et=class extends be{render(){if(!this.repository.installed)return P``;const e=this.hass.localize("component.hacs.repository.uninstall");return this.status.background_task?P`
                <mwc-button disabled>
                    ${e}
                </mwc-button>
            `:P`
            <mwc-button @click=${this.RepositoryUnInstall}">
                ${"uninstalling"==this.repository.state?P`<paper-spinner active></paper-spinner>`:P`${e}`}
            </mwc-button>
        `}static get styles(){return[ge,ce`
          mwc-button {
            --mdc-theme-primary: var(--google-red-500);
          }
        `]}RepositoryUnInstall(){window.confirm(this.hass.localize("component.hacs.confirm.uninstall","item",this.repository.name))&&this.ExecuteAction()}ExecuteAction(){we(this.hass,this.repository.id,"set_state","uninstalling"),we(this.hass,this.repository.id,"uninstall")}};Et=e([oe("hacs-button-uninstall")],Et);let zt=class extends be{constructor(){super(...arguments),this.pathExists=!1}firstUpdated(){this.hass.connection.sendMessagePromise({type:"hacs/check_path",path:this.repository.local_path}).then(e=>{this.pathExists=e.exist},e=>{console.error("[hacs/check_path] Message failed!",e)})}render(){const e=this.hass.localize(`component.hacs.repository.${this.repository.main_action.toLowerCase()}`);return this.status.background_task?P`
                <mwc-button disabled>
                    ${e}
                </mwc-button>
            `:P`
            <mwc-button
            @click=${this.RepositoryInstall}>
                ${"installing"==this.repository.state?P`<paper-spinner active></paper-spinner>`:P`${e}`}
            </mwc-button>
        `}RepositoryInstall(){this.repository.can_install?this.pathExists&&!this.repository.installed?window.confirm(this.hass.localize("component.hacs.confirm.exsist","item",this.repository.local_path)+"\n"+this.hass.localize("component.hacs.confirm.overwrite")+"\n"+this.hass.localize("component.hacs.confirm.continue"))&&this.ExecuteAction():this.ExecuteAction():window.alert(`This repository version requires Home Assistant version ${this.repository.homeassistant}`)}ExecuteAction(){we(this.hass,this.repository.id,"set_state","installing"),we(this.hass,this.repository.id,"install")}};e([ne()],zt.prototype,"pathExists",void 0),zt=e([oe("hacs-button-main-action")],zt);let Ct=class extends be{render(){if(!this.repository.pending_upgrade)return P``;var e=`https://github.com/${this.repository.full_name}/releases`;return"commit"===this.repository.version_or_commit&&(e=`https://github.com/${this.repository.full_name}/compare/${this.repository.installed_version}...${this.repository.available_version}`),P`
        <a href="${e}" rel='noreferrer' target="_blank">
          <mwc-button>
          ${this.hass.localize("component.hacs.repository.changelog")}
          </mwc-button>
        </a>
        `}RepositoryInstall(){we(this.hass,this.repository.id,"set_state","installing"),we(this.hass,this.repository.id,"uninstall")}};Ct=e([oe("hacs-button-changelog")],Ct);let Tt=class extends de{render(){return P`
            <div class="lovelace-hint">
                <p class="example-title">${this.hass.localize("component.hacs.repository.lovelace_instruction")}:</p>
                <pre id="LovelaceExample" class="yaml">
- url: /community_plugin/${this.repository.full_name.split("/")[1]}/${this.repository.file_name}
  type: ${void 0!==this.repository.javascript_type?P`${this.repository.javascript_type}`:P`${this.hass.localize("component.hacs.repository.lovelace_no_js_type")}`}</pre>

                <paper-icon-button
                    title="${this.hass.localize("component.hacs.repository.lovelace_copy_example")}"
                    icon="mdi:content-copy"
                    @click="${this.CopyToLovelaceExampleToClipboard}"
                    role="button"
                ></paper-icon-button>
            </div>
            `}CopyToLovelaceExampleToClipboard(e){var t=e.composedPath()[4].children[0].children[1].innerText;document.addEventListener("copy",e=>{e.clipboardData.setData("text/plain",t),e.preventDefault(),document.removeEventListener("copy",null)}),document.execCommand("copy")}static get styles(){return[ge,ce`
            .lovelace-hint {

            }
            .example-title {
                margin-block-end: 0em;
            }
            .yaml {
                font-family: monospace, monospace;
                font-size: 1em;
                border-style: solid;
                border-width: thin;
                margin: 0;
                overflow: auto;
                display: inline-flex;
                width: calc(100% - 46px);
                white-space: pre-wrap;
            }

        `]}};e([ne()],Tt.prototype,"hass",void 0),e([ne()],Tt.prototype,"configuration",void 0),e([ne()],Tt.prototype,"repository",void 0),Tt=e([oe("hacs-lovelace-hint")],Tt);let Rt=class extends de{render(){return P`
            <div class="repository-note">
            <p>${this.hass.localize("component.hacs.repository.note_installed")} '${this.repository.local_path}'

            ${"appdaemon"===this.repository.category?P`,
            ${this.hass.localize(`component.hacs.repository.note_${this.repository.category}`)}`:""}

            ${"integration"===this.repository.category?P`,
            ${this.hass.localize(`component.hacs.repository.note_${this.repository.category}`)}`:""}

            ${"plugin"===this.repository.category?P`,
            ${this.hass.localize(`component.hacs.repository.note_${this.repository.category}`)}`:""}

            .</p>

                ${"plugin"===this.repository.category?P`
                    <hacs-lovelace-hint
                        .hass=${this.hass}
                        .configuration=${this.configuration}
                        .repository=${this.repository}
                    ></hacs-lovelace-hint>
                `:""}
            </div>
            `}static get styles(){return[ge,ce`
            .repository-note {
                border-top: 1px solid var(--primary-text-color);
            }
            p {
                font-style: italic;
            }
        `]}};e([ne()],Rt.prototype,"hass",void 0),e([ne()],Rt.prototype,"configuration",void 0),e([ne()],Rt.prototype,"repository",void 0),Rt=e([oe("hacs-repository-note")],Rt);let Nt=class extends be{render(){return this.repository.installed?null===this.repository.javascript_type?P``:P`
            <mwc-button @click=${this.RepositoryAddToLovelace}>
                Add to Lovelace
            </mwc-button>
        `:P``}RepositoryAddToLovelace(){window.confirm("Do you want to add this to your lovelace resources?")&&this.hass.connection.sendMessagePromise({type:"lovelace/config",force:!1}).then(e=>{var t=e;const o={type:this.repository.javascript_type,url:`/community_plugin/${this.repository.full_name.split("/")[1]}/${this.repository.file_name}`};t.resources?t.resources.push(o):t.resources=[o],this.hass.callWS({type:"lovelace/config/save",config:t})},e=>{console.error(e)})}};e([ne()],Nt.prototype,"lovelaceconfig",void 0),e([ne()],Nt.prototype,"configuration",void 0),Nt=e([oe("hacs-button-add-to-lovelace")],Nt);let Mt=class extends de{render(){if(!this.repository.installed)return P``;var e="",t="",o="";if("pending-restart"==this.repository.status)o="alert",t="Restart pending",e="\n            You need to restart Home Assistant.\n            ";else if("plugin"==this.repository.category){if(void 0!==this.lovelaceconfig&&!this.status.background_task)fe(this.repository,this.lovelaceconfig,this.status)||(o="warning",t="Not Loaded",e="\n                    This plugin is not added to your Lovelace resources.\n                    ")}return 0==e.length?P``:"plugin"!==this.repository.category?P`
            <ha-card header="${t}" class="${o}">
                <div class="card-content">
                    ${e}
                </div>
            </ha-card>
            `:P`
            <ha-card header="${t}" class="${o}">
                <div class="card-content">
                    ${e}
                </div>
                <div class="card-actions">
                    <hacs-button-add-to-lovelace
                        .hass=${this.hass}
                        .configuration=${this.configuration}
                        .repository=${this.repository}
                        .lovelaceconfig=${this.lovelaceconfig}>
                    </hacs-button-add-to-lovelace>
                </div>
            </ha-card>
        `}static get styles(){return[ge,ce`
            ha-card {
                width: 90%;
                margin-left: 5%;
            }
            .alert {
                background-color: var(--hacs-status-pending-restart);
                color: var(--text-primary-color);
            }
            .warning {
                background-color: var(--hacs-status-pending-update)
                color: var(--primary-text-color);
            }
            .info {
                background-color: var(--primary-background-color)
                color: var(--primary-text-color);
            }
        `]}};e([ne()],Mt.prototype,"hass",void 0),e([ne()],Mt.prototype,"repository",void 0),e([ne()],Mt.prototype,"status",void 0),e([ne()],Mt.prototype,"configuration",void 0),e([ne()],Mt.prototype,"lovelaceconfig",void 0),Mt=e([oe("hacs-repository-banner-note")],Mt);let Pt=class extends de{constructor(){super(...arguments),this.repository_view=!1}firstUpdated(){void 0!==this.repo&&this.repo.updated_info||(we(this.hass,this.repository,"set_state","other"),we(this.hass,this.repository,"update"))}render(){if(void 0===this.repository)return P`
      <hacs-panel
        .hass=${this.hass}
        .configuration=${this.configuration}
        .repositories=${this.repositories}
        .panel=${this.panel}
        .route=${this.route}
        .status=${this.status}
        .repository_view=${this.repository_view}
        .repository=${this.repository}
        .lovelaceconfig=${this.lovelaceconfig}
      >
      </hacs-panel>
      `;var e=this.repository,t=this.repositories.filter((function(t){return t.id===e}));if(this.repo=t[0],void 0===this.repo)return P`<div class="loader"><paper-spinner active></paper-spinner></div>`;if(this.repo.installed)var o=this.hass.localize("component.hacs.common.installed");else{if("appdaemon"===this.repo.category)var r="appdaemon_apps";else r=`${this.repo.category}s`;o=this.hass.localize(`component.hacs.common.${r}`)}return P`

    <div class="getBack">
      <mwc-button @click=${this.GoBackToStore} title="${o}">
      <ha-icon  icon="mdi:arrow-left"></ha-icon>
        ${this.hass.localize("component.hacs.repository.back_to")}
        ${o}
      </mwc-button>
      ${"other"==this.repo.state?P`<div class="loader"><paper-spinner active></paper-spinner></div>`:""}
    </div>

    <hacs-repository-banner-note
      .hass=${this.hass}
      .status=${this.status}
      .repository=${this.repo}
      .lovelaceconfig=${this.lovelaceconfig}
      .configuration=${this.configuration}>
    </hacs-repository-banner-note>

    <ha-card header="${this.repo.name}">
      <hacs-repository-menu .hass=${this.hass} .repository=${this.repo}></hacs-repository-menu>


      <div class="card-content">

        <div class="description addition">
          ${this.repo.description}
        </div>

        <div class="information MobileGrid">
          ${this.repo.installed?P`
          <div class="version installed">
            <b>${this.hass.localize("component.hacs.repository.installed")}: </b> ${this.repo.installed_version}
          </div>
          `:""}

        ${"0"===String(this.repo.releases.length)?P`
              <div class="version-available">
                  <b>${this.hass.localize("component.hacs.repository.available")}: </b> ${this.repo.available_version}
              </div>
          `:P`
              <div class="version-available">
                  <paper-dropdown-menu @value-changed="${this.SetVersion}"
                    label="${this.hass.localize("component.hacs.repository.available")}:
                     (${this.hass.localize("component.hacs.repository.newest")}: ${this.repo.releases[0]})">
                      <paper-listbox slot="dropdown-content" selected="${this.repo.selected_tag}" attr-for-selected="value">
                          ${this.repo.releases.map(e=>P`<paper-item value="${e}">${e}</paper-item>`)}
                          ${"hacs/integration"!==this.repo.full_name?P`
                          <paper-item value="${this.repo.default_branch}">${this.repo.default_branch}</paper-item>
                          `:""}
                      </paper-listbox>
                  </paper-dropdown-menu>
              </div>`}
        </div>
        <hacs-authors .hass=${this.hass} .authors=${this.repo.authors}></hacs-authors>
      </div>


      <div class="card-actions MobileGrid">
        <hacs-button-main-action .hass=${this.hass} .repository=${this.repo} .status=${this.status}></hacs-button-main-action>
        <hacs-button-changelog .hass=${this.hass} .repository=${this.repo}></hacs-button-changelog>
        <hacs-button-open-repository .hass=${this.hass} .repository=${this.repo}></hacs-button-open-repository>
        ${"plugin"===this.repo.category?P`
          <hacs-button-open-plugin .hass=${this.hass} .repository=${this.repo}></hacs-button-open-plugin>
        `:""}
        <hacs-button-uninstall class="right" .hass=${this.hass} .repository=${this.repo} .status=${this.status}></hacs-button-uninstall>
      </div>

    </ha-card>

    <ha-card class="additional">
      <div class="card-content">
        <div class="more_info markdown-body">
        <style>${wt} ${vt}</style>
          ${class{static html(e){const t=document.createElement("div");return t.innerHTML=bt(xt(e)),t.style.cssText=`${wt} ${vt}`,P`${t}`}}.html(this.repo.additional_info||"")}
        </div>
      <hacs-repository-note
        .hass=${this.hass}
        .configuration=${this.configuration}
        .repository=${this.repo}
      ></hacs-repository-note>
      </div>
    </ha-card>
        `}SetVersion(e){e.detail.value.length>0&&(we(this.hass,this.repo.id,"set_state","other"),we(this.hass,this.repo.id,"set_version",e.detail.value))}GoBackToStore(){this.repository=void 0,this.repo.installed?this.panel="installed":this.panel=this.repo.category,ue(0,`/${this._rootPath}/${this.panel}`),this.requestUpdate()}get _rootPath(){return void 0===this.route.prefix.split("/")[1]?"hacs":this.route.prefix.split("/")[1]}static get styles(){return[ge,ce`
      .loader {
        background-color: var(--primary-background-color);
        height: 100%;
        width: 100%;
      }
      paper-spinner {
        position: absolute;
        top: 30%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 99;
        width: 150px;
        height: 150px;
    }
     paper-dropdown-menu {
        width: 80%;
     }
      .description {
        font-style: italic;
        padding-bottom: 16px;
      }
      .version {
        padding-bottom: 8px;
      }
      .options {
        float: right;
        width: 40%;
      }
      .information {
        width: 60%;
      }
      .additional {
        margin-bottom: 108px;
      }
      .getBack {
        margin-top: 8px;
        margin-bottom: 4px;
        margin-left: 5%;
      }
      .right {
        float: right;
      }
      .loading {
        text-align: center;
        width: 100%;
      }
      ha-card {
        width: 90%;
        margin-left: 5%;
      }
      .link-icon {
        color: var(--dark-primary-color);
        margin-right: 8px;
      }

    `]}};e([ne()],Pt.prototype,"hass",void 0),e([ne()],Pt.prototype,"repositories",void 0),e([ne()],Pt.prototype,"configuration",void 0),e([ne()],Pt.prototype,"repository",void 0),e([ne()],Pt.prototype,"panel",void 0),e([ne()],Pt.prototype,"route",void 0),e([ne()],Pt.prototype,"status",void 0),e([ne()],Pt.prototype,"repository_view",void 0),e([ne()],Pt.prototype,"repo",void 0),e([ne()],Pt.prototype,"lovelaceconfig",void 0),Pt=e([oe("hacs-panel-repository")],Pt);let Lt=class extends de{Delete(e){if(window.confirm(this.hass.localize("component.hacs.confirm.delete","item",e.composedPath()[3].innerText))){var t=e.composedPath()[4].repoID;we(this.hass,t,"delete")}}Save(e){var t=e.composedPath()[2].children[1].selectedItem.category,o=e.composedPath()[2].children[0].value;we(this.hass,o,"add",t)}render(){return this.custom=this.repositories.filter((function(e){return!!e.custom})),P`
        <ha-card header="${this.hass.localize("component.hacs.settings.custom_repositories")}">
            <div class="card-content">
            <div class="custom-repositories-list">

            ${this.status.background_task?P`

            `:P`
            ${this.custom.sort((e,t)=>e.full_name>t.full_name?1:-1).map(e=>P`
                <div class="row" .repoID=${e.id}>
                    <paper-item>
                        ${e.full_name}
                        <ha-icon
                        title="${this.hass.localize("component.hacs.settings.delete")}"
                        class="listicon" icon="mdi:delete"
                        @click=${this.Delete}
                        ></ha-icon>
                    </paper-item>
                </div>
                `)}
            `}

            </div>
            </div>

            <div class="card-actions">
                <paper-input class="inputfield MobileGrid" placeholder=${this.hass.localize("component.hacs.settings.add_custom_repository")} type="text"></paper-input>
                <paper-dropdown-menu class="category MobileGrid"
                label="${this.hass.localize("component.hacs.settings.category")}">
                  <paper-listbox slot="dropdown-content" selected="-1">
                      ${this.configuration.categories.map(e=>P`
                      <paper-item .category=${e}>
                        ${this.hass.localize(`component.hacs.common.${e}`)}
                      </paper-item>`)}
                  </paper-listbox>
              </paper-dropdown-menu>

              <div class="save">
                <ha-icon title="${this.hass.localize("component.hacs.settings.save")}"
                    icon="mdi:content-save"
                    class="saveicon MobileGrid"
                    @click=${this.Save}>
                </ha-icon>
            </div>

        </ha-card>
            `}static get styles(){return[ge,ce`
            ha-card {
                width: 90%;
                margin-left: 5%;
            }
            .custom-repositories {

            }
            .add-repository {

            }
            .inputfield {
                width: 60%;
            }
            .category {
                position: absolute;
                width: 30%;
                right: 54px;
                bottom: 5px;
            }
            .saveicon {
                color: var(--primary-color);
                position: absolute;
                right: 0;
                bottom: 24px;
                cursor: pointer;
            }
            .listicon {
                color: var(--primary-color);
                right: 0px;
                position: absolute;
                cursor: pointer;
            }
            .loading {
                position: absolute;
                right: 10px;
                bottom: 22px;
            }

            @media screen and (max-width: 600px) and (min-width: 0) {
                .saveicon {
                    height: 64px;
                }
                .save {
                    padding-bottom: 64px;
                }
            }
        `]}};e([ne()],Lt.prototype,"hass",void 0),e([ne()],Lt.prototype,"repositories",void 0),e([ne()],Lt.prototype,"custom",void 0),e([ne()],Lt.prototype,"status",void 0),e([ne()],Lt.prototype,"configuration",void 0),Lt=e([oe("hacs-custom-repositories")],Lt);let It=class extends de{UnHide(e){var t=e.composedPath()[4].repoID;we(this.hass,t,"unhide")}render(){return this._hidden=this.repositories.filter((function(e){return e.hide})),0===this._hidden.length?P``:P`
        <ha-card header="${this.hass.localize("component.hacs.settings.hidden_repositories").toUpperCase()}">
            <div class="card-content">
            <div class="custom-repositories-list">

            ${this._hidden.sort((e,t)=>e.full_name>t.full_name?1:-1).map(e=>P`
                <div class="row" .repoID=${e.id}>
                    <paper-item>
                    <ha-icon
                    title="${this.hass.localize("component.hacs.settings.unhide")}"
                    class="listicon" icon="mdi:restore"
                    @click=${this.UnHide}
                    ></ha-icon>
                        ${e.full_name}
                    </paper-item>
                </div>
                `)}
            </div>
            </div>
        </ha-card>
            `}static get styles(){return[ge,ce`
            ha-card {
                width: 90%;
                margin-left: 5%;
            }
            .listicon {
                color: var(--primary-color);
                left: 0px;
            }
        `]}};e([ne()],It.prototype,"hass",void 0),e([ne()],It.prototype,"repositories",void 0),e([ne()],It.prototype,"_hidden",void 0),It=e([oe("hacs-hidden-repositories")],It);let Bt=class extends de{render(){return P`

    <ha-card header="${this.hass.localize("component.hacs.config.title")}">
      <div class="card-content">
        <p><b>${this.hass.localize("component.hacs.common.version")}:</b> ${this.configuration.version}</p>
        <p><b>${this.hass.localize("component.hacs.common.repositories")}:</b> ${this.repositories.length}</p>
        <div class="version-available">
        <ha-switch
          .checked=${"Table"===this.configuration.frontend_mode}
          @change=${this.SetFeStyle}
        >${this.hass.localize("component.hacs.settings.table_view")}</ha-switch>
        ${this.configuration.experimental?P`
          <ha-switch
            .checked=${this.configuration.frontend_compact}
            @change=${this.SetFeCompact}
          >${this.hass.localize("component.hacs.settings.compact_mode")}</ha-switch>
        `:""}

    </div>
      </div>
      <div class="card-actions MobileGrid">

      ${this.status.reloading_data?P`
        <mwc-button  disabled>
          <paper-spinner active></paper-spinner>
        </mwc-button>
      `:P`
      ${this.status.background_task?P`
        <mwc-button disabled>
          ${this.hass.localize("component.hacs.settings.reload_data")}
        </mwc-button>
      `:P`
        <mwc-button @click=${this.UpgradeAll}>
          ${this.hass.localize("component.hacs.settings.reload_data")}
        </mwc-button>
      `}
      `}


      ${this.status.upgrading_all?P`
          <mwc-button  disabled>
            <paper-spinner active></paper-spinner>
          </mwc-button>
      `:P`
      ${this.status.background_task?P`
        <mwc-button disabled>
          ${this.hass.localize("component.hacs.settings.upgrade_all")}
        </mwc-button>
      `:P`
        <mwc-button @click=${this.UpgradeAll}>
          ${this.hass.localize("component.hacs.settings.upgrade_all")}
        </mwc-button>
      `}
      `}

      <a href="https://github.com/hacs/integration" target="_blank" rel="noreferrer">
        <mwc-button >
          ${this.hass.localize("component.hacs.settings.hacs_repo")}
        </mwc-button>
      </a>

      <a href="https://github.com/hacs/integration/issues" target="_blank" rel="noreferrer">
        <mwc-button >
          ${this.hass.localize("component.hacs.repository.open_issue")}
        </mwc-button>
      </a>
      </div>
    </ha-card>
    <hacs-custom-repositories
      .hass=${this.hass}
      .status=${this.status}
      .configuration=${this.configuration}
      .repositories=${this.repositories}
    >
    </hacs-custom-repositories>
    <hacs-hidden-repositories
    .hass=${this.hass}
    .status=${this.status}
    .configuration=${this.configuration}
    .repositories=${this.repositories}
    >
    </hacs-hidden-repositories
          `}SetFeStyle(){this.hass.connection.sendMessage({type:"hacs/settings",action:`set_fe_${"Table"!==this.configuration.frontend_mode?"table":"grid"}`})}SetFeCompact(){this.hass.connection.sendMessage({type:"hacs/settings",action:`set_fe_compact_${String(this.configuration.frontend_compact).toLocaleLowerCase()}`})}ReloadData(){this.hass.connection.sendMessage({type:"hacs/settings",action:"reload_data"})}UpgradeAll(){var e=[];if(this.repositories.forEach(t=>{t.pending_upgrade&&e.push(t)}),e.length>0){var t="This will upgrade all of these repositores, make sure that you have read the release notes for all of them before proceeding.";if(t+="\n",t+="\n",e.forEach(e=>{t+=`${e.name} ${e.installed_version} -> ${e.available_version}\n`}),!window.confirm(t))return;this.hass.connection.sendMessage({type:"hacs/settings",action:"upgrade_all"})}else window.alert("No upgrades pending")}static get styles(){return[ge,ce`
    ha-card {
      width: 90%;
      margin-left: 5%;
    }
    ha-switch {
      margin-bottom: 8px;
    }
    mwc-button {
      margin: 0 8px 0 8px;
    }
    `]}};e([ne()],Bt.prototype,"hass",void 0),e([ne()],Bt.prototype,"repositories",void 0),e([ne()],Bt.prototype,"configuration",void 0),e([ne()],Bt.prototype,"status",void 0),Bt=e([oe("hacs-panel-settings")],Bt);let Ot=class extends de{render(){return this.status.background_task?P`
            <paper-progress indeterminate></paper-progress>
        `:P``}static get styles(){return[ge,ce`
            paper-progress {
                width: 100%;
                --paper-progress-active-color: var(--accent-color);
            }
        `]}};e([ne()],Ot.prototype,"status",void 0),Ot=e([oe("hacs-progressbar")],Ot);let Dt=class extends de{constructor(){super(...arguments),this.error=void 0}clearError(){this.error=void 0}firstUpdated(){this.hass.connection.subscribeEvents(e=>this.error=e.data,"hacs/error")}render(){if(void 0===this.error)return P``;var e=this.error.message,t="";return"add_repository"===this.error.action&&(t="Could not add this repository, make sure it is compliant with HACS."),P`
            <ha-card header="An error ocoured while prosessing" class="alert">
                <div class="card-content">
                    ${e} </br>
                    ${t}
                </div>
            <div class="card-actions">
                <mwc-button @click=${this.clearError}>
                    Acknowledge
                </mwc-button>
            ${"add_repository"===this.error.action?P`
            <a href="https://hacs.xyz/docs/publish/start" rel='noreferrer' target="_blank">
                <mwc-button>
                    Documentation
                </mwc-button>
            </a>
            `:""}
            </div>
            </ha-card>
            `}static get styles(){return[ge,ce`
            ha-card {
                width: 90%;
                margin-left: 5%;
            }
            .alert {
                background-color: var(--hacs-status-pending-restart);
                color: var(--text-primary-color);
            }
        `]}};e([ne()],Dt.prototype,"hass",void 0),e([ne()],Dt.prototype,"error",void 0),Dt=e([oe("hacs-error")],Dt);let jt=class extends de{async Acknowledge(e){var t=e.composedPath()[3].repository;const o=await this.hass.connection.sendMessagePromise({type:"hacs/critical",repository:t});this.critical=o.data}render(){if(void 0===this.critical)return P``;var e=[];return this.critical.forEach(t=>{t.acknowledged||e.push(t)}),P`
            ${e.map(e=>P`
            <ha-card header="Critical Issue!" class="alert">
                <div class="card-content">
                    The repository "${e.repository}" has been flagged as a critical repository.</br>
                    The repository has now been uninstalled and removed.</br>
                    For information about how and why these are handled, see
                    <a href="https://hacs.xyz/docs/developer/maintaner#critical-repositories">
                        https://hacs.xyz/docs/developer/maintaner#critical-repositories
                    </a></br>
                    As a result of this Home Assistant was also restarted.</br></br>

                    <b>Reason: </b>${e.reason}
                </div>
                <div class="card-actions">
                    <mwc-button @click=${this.Acknowledge} .repository=${e.repository}>
                        Acknowledge
                    </mwc-button>
                    <a href="${e.link}" rel='noreferrer' target="_blank">
                        <mwc-button>
                            More information about this incident
                        </mwc-button>
                    </a>
                </div>
            </ha-card>`)}
            `}static get styles(){return[ge,ce`
            ha-card {
                width: 90%;
                margin-left: 5%;
            }
            .alert {
                background-color: var(--hacs-status-pending-restart);
                color: var(--text-primary-color);
            }
        `]}};e([ne()],jt.prototype,"hass",void 0),e([ne()],jt.prototype,"critical",void 0),jt=e([oe("hacs-critical")],jt);let Ut=class extends de{constructor(){super(...arguments),this.repository_view=!1}getRepositories(){this.hass.connection.sendMessagePromise({type:"hacs/repositories"}).then(e=>{this.repositories=e,this.requestUpdate()},e=>{console.error("[hacs/repositories] Message failed!",e)})}getConfig(){this.hass.connection.sendMessagePromise({type:"hacs/config"}).then(e=>{this.configuration=e,this.requestUpdate()},e=>{console.error("[hacs/config] Message failed!",e)})}getCritical(){this.hass.connection.sendMessagePromise({type:"hacs/get_critical"}).then(e=>{this.critical=e,this.requestUpdate()},e=>{console.error("[hacs/get_critical] Message failed!",e)})}getStatus(){this.hass.connection.sendMessagePromise({type:"hacs/status"}).then(e=>{this.status=e,this.requestUpdate()},e=>{console.error("[hacs/status] Message failed!",e)})}getLovelaceConfig(){this.hass.connection.sendMessagePromise({type:"lovelace/config",force:!1}).then(e=>{this.lovelaceconfig=e},()=>{this.lovelaceconfig=void 0})}firstUpdated(){window.onpopstate=function(){window.location.reload()},localStorage.setItem("hacs-search",""),this.panel=this._page,this.getRepositories(),this.getConfig(),this.getStatus(),this.getCritical(),this.getLovelaceConfig(),/repository\//i.test(this.route.path)?(this.repository_view=!0,this.repository=this.route.path.split("/")[2]):this.repository_view=!1,he(),this.hass.connection.subscribeEvents(()=>this.getRepositories(),"hacs/repository"),this.hass.connection.subscribeEvents(()=>this.getConfig(),"hacs/config"),this.hass.connection.subscribeEvents(()=>this.getStatus(),"hacs/status"),this.hass.connection.subscribeEvents(e=>this._reload(e),"hacs/reload"),this.hass.connection.subscribeEvents(()=>this.getLovelaceConfig(),"lovelace_updated")}_reload(e){window.location.reload(e.data.force)}render(){if(""===this.panel&&(ue(0,`/${this._rootPath}/installed`),this.panel="installed"),void 0===this.repositories||void 0===this.configuration||void 0===this.status)return P`<div  class="loader"><paper-spinner active></paper-spinner></div>`;/repository\//i.test(this.route.path)?(this.repository_view=!0,this.repository=this.route.path.split("/")[2],this.panel="repository"):this.repository_view=!1;const e=this.panel;return P`
    <app-header-layout has-scrolling-region>
      <app-header slot="header" fixed>
        <app-toolbar>
        <ha-menu-button .hass="${this.hass}" .narrow="${this.narrow}"></ha-menu-button>
          <div main-title>Home Assistant Community Store
          ${"hacs_dev"===this._rootPath?P`(DEVELOPMENT)`:""}
          </div>
        </app-toolbar>
      <paper-tabs scrollable attr-for-selected="page-name" .selected=${e} @iron-activate=${this.handlePageSelected}>

        <paper-tab page-name="installed">${this.hass.localize("component.hacs.common.installed")}</paper-tab>

        <paper-tab page-name="integration">${this.hass.localize("component.hacs.common.integrations")}</paper-tab>

        <paper-tab page-name="plugin">${this.hass.localize("component.hacs.common.plugins")}</paper-tab>

        ${this.configuration.appdaemon?P`<paper-tab page-name="appdaemon">
            ${this.hass.localize("component.hacs.common.appdaemon_apps")}
        </paper-tab>`:""}

        ${this.configuration.python_script?P`<paper-tab page-name="python_script">
            ${this.hass.localize("component.hacs.common.python_scripts")}
        </paper-tab>`:""}

        ${this.configuration.theme?P`<paper-tab page-name="theme">
            ${this.hass.localize("component.hacs.common.themes")}
        </paper-tab>`:""}

        <paper-tab page-name="settings">${this.hass.localize("component.hacs.common.settings")}</paper-tab>
      </paper-tabs>
    </app-header>

    <hacs-progressbar .status=${this.status}></hacs-progressbar>

    <hacs-critical .hass=${this.hass} .critical=${this.critical}></hacs-critical>
    <hacs-error .hass=${this.hass}></hacs-error>

    ${"settings"!==this.panel?P`
      <hacs-panel
        .hass=${this.hass}
        .configuration=${this.configuration}
        .repositories=${this.repositories}
        .panel=${this.panel}
        .route=${this.route}
        .status=${this.status}
        .repository_view=${this.repository_view}
        .repository=${this.repository}
        .lovelaceconfig=${this.lovelaceconfig}
      >
      </hacs-panel>`:P`
      <hacs-panel-settings
        .hass=${this.hass}
        .status=${this.status}
        .configuration=${this.configuration}
        .repositories=${this.repositories}>
      </hacs-panel-settings>`}
      <hacs-help-button></hacs-help-button>
    </app-header-layout>`}handlePageSelected(e){this.repository_view=!1;const t=e.detail.selected;this.panel=t,this.route.path=`/${t}`,ue(0,`${this.route.prefix}${this.route.path}`),function(e,t){const o=t,r=Math.random(),i=Date.now(),n=o.scrollTop,s=0-n;e._currentAnimationId=r,function t(){const a=Date.now()-i;var l;a>200?o.scrollTop=0:e._currentAnimationId===r&&(o.scrollTop=(l=a,-s*(l/=200)*(l-2)+n),requestAnimationFrame(t.bind(e)))}.call(e)}(this,this.shadowRoot.querySelector("app-header-layout").header.scrollTarget)}get _page(){return void 0===this.route.path.split("/")[1]?"installed":this.route.path.split("/")[1]}get _rootPath(){return void 0===this.route.prefix.split("/")[1]?"hacs":this.route.prefix.split("/")[1]}static get styles(){return[ge,ce`
    .loader {
      background-color: var(--primary-background-color);
      height: 100%;
      width: 100%;
    }
    paper-spinner {
      position: absolute;
      top: 30%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 99;
      width: 150px;
      height: 150px;
   }
    `]}};e([ne()],Ut.prototype,"hass",void 0),e([ne()],Ut.prototype,"repositories",void 0),e([ne()],Ut.prototype,"configuration",void 0),e([ne()],Ut.prototype,"status",void 0),e([ne()],Ut.prototype,"route",void 0),e([ne()],Ut.prototype,"critical",void 0),e([ne()],Ut.prototype,"narrow",void 0),e([ne()],Ut.prototype,"panel",void 0),e([ne()],Ut.prototype,"repository",void 0),e([ne()],Ut.prototype,"repository_view",void 0),e([ne()],Ut.prototype,"lovelaceconfig",void 0),Ut=e([oe("hacs-frontend")],Ut);
