edjs=function () {
    var QWindow=winjs.QWindow;
    class Editor {
        constructor(el, content) {
            if ((el != null) && ($.isPlainObject(el))) {
                this.el = el.el;
                this.init_content = el.content ;
            } else {
                this.el = el;
                this.init_content = content ;
            }
            this.init_content=this.init_content || this.el.html() || 'Write some thing here...';
            this.el.html(this.html());
            this.window=new QWindow({el:this.el,title:'Editor'});

            this.content_box=this.el.find('.editor-area');
            this.hide();
        }
        hide(){
            this.window.hide();
        }
        show(){
            this.window.show();
        }
        add_content(cont){
            console.log(this.content_box)
            return this.content_box.html(cont);
        }
        html(){
            return `<div class="editor-area" contenteditable="true">${this.init_content}</div>`
        }
    }
    return{
        Editor:Editor
    }
}();