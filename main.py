import reflex as rx

class FireControlState(rx.State):
    # Form Input Coordinates
    cannon_x: float = 0.0
    cannon_z: float = 0.0
    target_x: float = 100.0
    target_z: float = 100.0
    
    # Target calculations
    @rx.var
    def delta_x(self) -> float:
        return self.target_x - self.cannon_x

    @rx.var
    def delta_z(self) -> float:
        return self.target_z - self.cannon_z

    @rx.var
    def required_tnt(self) -> float:
        # Insert your dynamic motion/trajectory vector scaling here
        # Example formula: distance divided by standard acceleration multiplier
        distance = (self.delta_x**2 + self.delta_z**2) ** 0.5
        return round(distance * 0.75, 2)

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("OSC FIRE CONTROL SYSTEM", size="8", color_scheme="crimson"),
            rx.text("Calculate trajectories and firing solutions for coordinate shifts.", color_scheme="gray"),
            
            rx.divider(),
            
            # Position Inputs
            rx.hstack(
                rx.vstack(
                    rx.text("Cannon X"),
                    rx.input(value=FireControlState.cannon_x, on_change=FireControlState.set_cannon_x, type="number"),
                ),
                rx.vstack(
                    rx.text("Cannon Z"),
                    rx.input(value=FireControlState.cannon_z, on_change=FireControlState.set_cannon_z, type="number"),
                ),
                spacing="4"
            ),
            
            rx.hstack(
                rx.vstack(
                    rx.text("Target X"),
                    rx.input(value=FireControlState.target_x, on_change=FireControlState.set_target_x, type="number"),
                ),
                rx.vstack(
                    rx.text("Target Z"),
                    rx.input(value=FireControlState.target_z, on_change=FireControlState.set_target_z, type="number"),
                ),
                spacing="4"
            ),
            
            rx.divider(),
            
            # Dynamic Results Output Card
            rx.card(
                rx.vstack(
                    rx.heading("Firing Solution Outputs", size="4"),
                    rx.text(f"ΔX Vector: {FireControlState.delta_x}"),
                    rx.text(f"ΔZ Vector: {FireControlState.delta_z}"),
                    rx.text(f"Estimated TNT Charge Needed: {FireControlState.required_tnt} blocks", font_weight="bold", color="red"),
                    align="start",
                    spacing="2"
                ),
                width="100%",
                background_color="rgba(0, 0, 0, 0.2)"
            ),
            
            spacing="6",
            padding="8",
            background_color="neutral",
            border_radius="lg",
            box_shadow="xl",
            max_width="500px",
        ),
        padding_top="10%"
    )

app = rx.App(theme=rx.theme(appearance="dark")) # Forces dark theme like cubicmetre's app
app.add_page(index)
