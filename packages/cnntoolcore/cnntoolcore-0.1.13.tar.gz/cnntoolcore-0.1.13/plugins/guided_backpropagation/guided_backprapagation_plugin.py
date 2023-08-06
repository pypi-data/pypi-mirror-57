import torch

from visualization_core.interfaces.VisualizationTechnique import GraphVisualizationTechnique, PrintingMode
from visualization_utils.extractors.gradient_extractor import GradientExtractor
from visualization_utils.hook_utils import HookUtils


class GuidedBackpropagationPlugin(GraphVisualizationTechnique):
    def __init__(self) -> None:
        super().__init__('guided_backpropagation')
        self.module_forward_zeros_positions_map = {}
        self.module_output_gradient_map = {}

    def is_applicable_for(self, model):
        return True

    def get_printing_mode(self):
        return PrintingMode.NORMAL

    # Image tensor should be preporcessed
    def get_module_visualizations_list_map(self, model, image_tensor, class_index_vector):
        HookUtils.deep_hook_register_for_subtype(model, self.forward_zero_positions_storing_hook, 'forward')
        HookUtils.deep_hook_register_for_subtype(model, self.gradient_hook, 'backward')


    def forward_zero_positions_storing_hook(self, module, input, output):
        if module not in self.module_forward_zeros_positions_map.keys():
            self.module_forward_zeros_positions_map[module] = []

        for i in range(output.shape[1]):
            self.module_forward_zeros_positions_map[module].append(torch.tensor(output[0][i] >= 0, dtype=torch.float32))

    def gradient_hook(self, module, input, output):
        if module not in self.module_output_gradient_map.keys():
            self.module_output_gradient_map[module] = []

        for i in range(output.shape[1]):
            self.module_output_gradient_map[module].append(output[0][i])