import dash
import dash_bio
import dash_html_components as html

from common_features import simple_app_layout, simple_app_callback, \
    user_interactions_layout, user_interactions_callback

_COMPONENT_ID = 'myigv'

igvStyle = dict(
    paddingTop='10px',
    paddingBottom='10px',
    margin='8px',
    border='1px solid lightgray'
)


def test_ASM985889v3(dash_duo):
    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.Igv(
            id=_COMPONENT_ID,
            reference={
                "id": "ASM985889v3",
                "name": "Sars-CoV-2 (ASM985889v3)",
                "fastaURL": "https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna",
                "indexURL": "https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna.fai",
                "order": 1000000,
                "tracks": [
                    {
                        "name": "Annotations",
                        "url": "https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz",
                        "displayMode": "EXPANDED",
                        "nameField": "gene",
                        "height": 150
                    }
                ]

            },
            minimumBases=100,
            style=igvStyle
        ),
    ))

    dash_duo.start_server(app)

    # Check that the genome loaded
    dash_duo.wait_for_text_to_equal('#igv-current_genome', 'ASM985889v3')

    # Check that track(s) loaded
    tracks = dash_duo.find_elements('.igv-track-label')
    assert len(tracks) == 1
    assert tracks[0].text == 'Annotations'


def test_ASM985889v3_tracks(dash_duo):
    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.Igv(
            id=_COMPONENT_ID,
            reference={
                "id": "ASM985889v3",
                "name": "Sars-CoV-2 (ASM985889v3)",
                "fastaURL": "https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna",
                "indexURL": "https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna.fai",
                "order": 1000000,
                "tracks": [
                    {
                        "name": "Annotations",
                        "url": "https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz",
                        "displayMode": "EXPANDED",
                        "nameField": "gene",
                        "height": 150
                    }
                ]

            },
            tracks=[{  # normally, tracks listed here would not duplicate those already present above

                "name": "Genes",
                "type": "annotation",
                "url": "https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz",
                "displayMode": "EXPANDED"

            }],
            minimumBases=100,
            style=igvStyle
        ),
    ))

    dash_duo.start_server(app)

    # Check that the genome loaded
    dash_duo.wait_for_text_to_equal('#igv-current_genome', 'ASM985889v3')

    # Check that track(s) loaded
    tracks = dash_duo.find_elements('.igv-track-label')
    assert tracks[0].text == 'Annotations'
    assert tracks[1].text == 'Genes'


def test_sacCer3(dash_duo):
    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.Igv(
            id=_COMPONENT_ID,
            reference={
                "id": "sacCer3",
                "name": "S. cerevisiae (sacCer3)",
                "fastaURL": "https://s3.dualstack.us-east-1.amazonaws.com/igv.org.genomes/sacCer3/sacCer3.fa",
                "indexURL": "https://s3.dualstack.us-east-1.amazonaws.com/igv.org.genomes/sacCer3/sacCer3.fa.fai",
                "tracks": [
                    {
                        "name": "Ensembl Genes",
                        "type": "annotation",
                        "format": "ensgene",
                        "displayMode": "EXPANDED",
                        "url": "https://s3.dualstack.us-east-1.amazonaws.com/igv.org.genomes/sacCer3/ensGene.txt.gz",
                        "indexed": False,
                        "supportsWholeGenome": False
                    }
                ]
            },
            minimumBases=100,
            style=igvStyle
        ),
    ))

    dash_duo.start_server(app)

    # Check that the genome loaded
    dash_duo.wait_for_text_to_equal('#igv-current_genome', 'sacCer3')

    # Check that track(s) loaded
    tracks = dash_duo.find_elements('.igv-track-label')
    assert len(tracks) == 1
    assert tracks[0].text == 'Ensembl Genes'
