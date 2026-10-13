from dataclasses import dataclass

@dataclass
class Router:
    def route(self):
        raise NotImplementedError

@dataclass
class VoLTE(Router):
    def route(self):
        print("Routing through VoLTE")

@dataclass
class FourG(Router):
    def route(self):
        print("Routing through 4G")

@dataclass
class FiveG(Router):
    def route(self):
        print("Routing through 5G")

@dataclass
class Wifi(Router):
    def route(self):
        print("Routing through Wifi")

@dataclass
class RouterService:
    strategy: Router
    
    def route(self):
        self.strategy.route()

router = RouterService(FiveG())
router.route()

router.strategy = VoLTE()
router.route()