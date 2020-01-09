CKEDITOR.editorConfig = function( config ) {
    var ArticleEditToolbar = [
        {name: 'document', items: ['Preview']},
        {name: 'clipboard', items: ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
        {name: 'editing', items: ['Find', 'Replace', '-', 'SelectAll']},
        {name: 'styles', items: ['Styles', 'Format', 'Font', 'FontSize']},
        {name: 'basicstyles',
         items: ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat']}, 
        '/',
        {name: 'colors', items: ['TextColor', 'BGColor']},
        {name: 'paragraph',
         items: ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                   'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'Blockquote']},
        {name: 'links', items: ['Link', 'Unlink', 'Anchor']},
        {name: 'insert', items: ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'Iframe']},
        {name: 'tools', items: ['Maximize', 'ShowBlocks']}
    ];

    config.toolbar = ArticleEditToolbar;
    config.height = 300;
	config.width = '100%';
};


