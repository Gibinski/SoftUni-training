class HDMIMixin:
    def connect_to_device_via_hdmi_cable(self): 
        pass


class RCAMixin:
    def connect_to_device_via_rca_cable(self): 
        pass


class EthernetMixin:
    def connect_to_device_via_ethernet_cable(self,):
        pass


class PoweOutletMixin:
    def connect_device_to_power_outlet(self): 
        pass


class Television(HDMIMixin, RCAMixin, PoweOutletMixin):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMIMixin, PoweOutletMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(HDMIMixin, EthernetMixin, PoweOutletMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EthernetMixin, PoweOutletMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
