import gradio as gr
import hydra
import pyrootutils
from omegaconf import DictConfig

from models.Searcher import Searcher

pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)


@hydra.main(config_path="../configs", config_name="config.yaml")
def run_gradio(cfg: DictConfig):
    api_key_input = gr.inputs.Textbox(label="API KEY")
    query_input = gr.inputs.Textbox(lines=3, label="query")
    result_output = gr.outputs.Textbox(label="Search result")
    searcher = Searcher(cfg.model)

    interface = gr.Interface(
        fn=searcher.search, inputs=[api_key_input, query_input], outputs=result_output
    )

    interface.launch(share=True)


if __name__ == "__main__":
    run_gradio()
