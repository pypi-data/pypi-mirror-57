import torch
from torch.nn import ReLU

from visualization_core.interfaces.VisualizationTechnique import GraphVisualizationTechnique
from visualization_utils.hook_utils import HookUtils


class GuidedBackprop(GraphVisualizationTechnique):

    def __init__(self) -> None:
        super().__init__('guided_backpropagation')
        self.forward_relu_outputs = []
        self.module_grad_outputs = {}


    def relu_backward_hook_function(self,module, grad_in, grad_out):

        if isinstance(module, ReLU):
            corresponding_forward_output = self.forward_relu_outputs[-1]
            corresponding_forward_output[corresponding_forward_output > 0] = 1
            modified_grad_out = corresponding_forward_output * torch.clamp(grad_in[0], min=0.0)
            del self.forward_relu_outputs[-1]  # Remove last forward output
            #Modified grad output is taken as next layer input
            if module not in self.module_grad_outputs.keys():
                self.module_grad_outputs[module] = []

            for i in range(modified_grad_out.shape[1]):
                self.module_grad_outputs[module].append(modified_grad_out[0][i])

            return (modified_grad_out,)
        else:
            if module not in self.module_grad_outputs.keys():
                self.module_grad_outputs[module] = []

            for i in range(grad_in.shape[0][1]):
                self.module_grad_outputs[module].append(grad_in[0][0][i])

    def relu_forward_hook_function(self,module, ten_in, ten_out):

        if isinstance(module, ReLU):
            self.forward_relu_outputs.append(ten_out)


    def get_module_visualizations_list_map(self, model, image_tensor, class_index_vector):
        HookUtils.deep_hook_register_for_subtype(model,self.relu_forward_hook_function, ReLU, 'forward')
        HookUtils.deep_hook_register_for_subtype(model,self.relu_backward_hook_function, ReLU, 'backward')

        model_output = model(image_tensor)
        model.zero_grad()
        model_output.backward(gradient=class_index_vector)
        return self.module_grad_outputs



