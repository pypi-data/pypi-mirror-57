from plugins_management.plugin_repository import get_plugin_repository
from visualization_core.interfaces.VisualizationTechnique import NonGraphVisualizationTechnique, \
    GraphVisualizationTechnique


class PluginSelector():
    @staticmethod
    def get_all_plugin_names():
        return [plugin.name for plugin in get_plugin_repository().get_all_plugins()]

    @staticmethod
    def get_selected_plugins(name_list):
        repository = get_plugin_repository()
        return [repository.get_plugin(name) for name in name_list]

    @staticmethod
    def get_all_graph_visualization_plugins():
        return [plugin.name for plugin in get_plugin_repository().get_all_plugins() if issubclass(plugin.__class__, GraphVisualizationTechnique)]

    @staticmethod
    def get_all_non_graph_visualization_plugins():
        return [plugin.name for plugin in get_plugin_repository().get_all_plugins() if issubclass(plugin.__class__, NonGraphVisualizationTechnique)]