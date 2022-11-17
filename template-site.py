import flask

def main():
    app = flask.Flask(
        'Meu Servidor',
        template_folder='TEMPLATES',
        static_folder='FODA'
    )

    @app.route('/', methods = ['GET'])
    def main_page():
        return flask.render_template(
            'template3.html',
             meu_novo_paragrafo='<p>Toma deles</p>'
        )

    app.run(debug = True)


if __name__ == '__main__':
    main()