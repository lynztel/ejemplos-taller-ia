from manim import *


BG = "#102E36"
CARD = "#16474B"
MINT = "#C9F279"
TEAL = "#53B8A7"
GOLD = "#EAB755"
PAPER = "#F4F6F1"
MUTED = "#B8C9C1"
FONT = "Arial"


def text(label, size, color=PAPER, weight=NORMAL):
    return Text(label, font=FONT, font_size=size, color=color, weight=weight)


def heading(scene, title, kicker):
    scene.camera.background_color = BG
    top = text(kicker.upper(), 20, MINT, BOLD).to_edge(UP, buff=0.42)
    headline = text(title, 38, PAPER, BOLD).next_to(top, DOWN, buff=0.22)
    scene.play(FadeIn(top, shift=DOWN * 0.12), Write(headline), run_time=0.8)


def metric_card(title, headline, detail, color=MINT, width=4.35):
    card = RoundedRectangle(
        width=width, height=3.8, corner_radius=0.2,
        stroke_color="#37676A", stroke_width=2, fill_color=CARD, fill_opacity=1,
    )
    title_mob = text(title.upper(), 16, MUTED, BOLD)
    main = text(headline, 34, color, BOLD)
    sub = text(detail, 16, PAPER)
    group = VGroup(title_mob, main, sub).arrange(DOWN, buff=0.34)
    group.move_to(card.get_center())
    return VGroup(card, group)


class HoursComparison(Scene):
    def construct(self):
        heading(self, "¿Cuánto tiempo quieres dedicar?", "Clases individuales en línea · CDMX")
        part = metric_card("Medio tiempo usado en el modelo", "40 h / mes", "≈ 9.2 h por semana", MINT)
        half = metric_card("Media jornada convencional", "20 h / semana", "≈ 86.7 h por mes", GOLD)
        full = metric_card("Tiempo completo", "40 h / semana", "≈ 173.3 h por mes", TEAL)
        cards = VGroup(part, half, full).arrange(RIGHT, buff=0.16).shift(DOWN * 0.2)
        self.play(FadeIn(cards, shift=UP * 0.12), run_time=0.7)
        note = text("Tiempo completo = 8 h/día × 5 días/semana. Promedio mensual: 52/12 semanas.", 16, MUTED).to_edge(DOWN, buff=0.32)
        self.play(FadeIn(note), run_time=0.45)
        self.wait(8.05)


class DemandIncome(Scene):
    def construct(self):
        heading(self, "La demanda supuesta da $6,000 en los tres casos", "Ingreso bruto mensual · escenario base")
        part = metric_card("40 h / mes", "$6,000", "24 clases × $250", MINT)
        half = metric_card("20 h / semana", "$6,000", "24 clases × $250", GOLD)
        full = metric_card("40 h / semana", "$6,000", "24 clases × $250", TEAL)
        cards = VGroup(part, half, full).arrange(RIGHT, buff=0.16).shift(UP * 0.2)
        self.play(FadeIn(cards, shift=UP * 0.12), run_time=0.7)
        note = text("La demanda parte de una hipótesis; más horas disponibles no crean estudiantes automáticamente.", 16, GOLD)
        note.move_to(DOWN * 2.35)
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.5)
        self.wait(8.0)


class CapacityCeiling(Scene):
    def construct(self):
        heading(self, "El techo cambia si llenas la agenda", "Capacidad máxima · no es una previsión de ventas")
        part = metric_card("40 clases · 40 h/mes", "$10,000", "40 h × $250 por clase", MINT)
        half = metric_card("87 clases · media jornada", "$21,667", "86.7 h × $250 por clase", GOLD)
        full = metric_card("173 clases · tiempo completo", "$43,333", "173.3 h × $250 por clase", TEAL)
        cards = VGroup(part, half, full).arrange(RIGHT, buff=0.16).shift(UP * 0.2)
        self.play(FadeIn(cards, shift=UP * 0.12), run_time=0.7)
        note = text("Ingreso bruto antes de costos, impuestos y pago por el tiempo de preparación.", 16, GOLD)
        note.move_to(DOWN * 2.35)
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.5)
        self.wait(8.0)


class CarGoal(Scene):
    def construct(self):
        heading(self, "Una meta que también se calcula", "Ahorro proyectado · revisa los supuestos")
        photo = ImageMobject("presentacion/assets/byd-dolphin-mini.webp").set_width(7.25)
        photo.to_edge(LEFT, buff=0.65).shift(DOWN * 0.38)
        frame = SurroundingRectangle(photo, color="#D6E8E1", buff=0.05, stroke_width=2)
        copy = VGroup(
            text("BYD DOLPHIN MINI", 20, MUTED, BOLD),
            text("Desde $399,800", 38, MINT, BOLD),
            text("Precio de referencia publicado.", 18, PAPER),
            text("El dashboard recalcula el plazo con tus horas, tarifa, costos y ahorro.", 17, PAPER),
            text("Internet pendiente en el escenario base.", 16, GOLD, BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        copy.set_width(5.45).to_edge(RIGHT, buff=0.7).shift(DOWN * 0.25)
        self.play(FadeIn(photo), Create(frame), run_time=0.7)
        self.play(FadeIn(copy, shift=LEFT * 0.12), run_time=0.6)
        self.wait(7.9)


class MarketOptions(Scene):
    def construct(self):
        heading(self, "Tres rutas para probar otra oferta", "Señales de precio publicado · no son ventas")
        interview = metric_card("Entrevistas y primer empleo", "$475 / h", "Ejemplo 1:1 con apoyo para CV", MINT)
        exam = metric_card("Preparación IELTS", "$7,435", "32 horas · máximo 16 estudiantes", GOLD)
        group = metric_card("Grupo corporativo online", "$400 / h", "Hasta 8 alumnos por grupo", TEAL)
        cards = VGroup(interview, exam, group).arrange(RIGHT, buff=0.16).shift(UP * 0.2)
        self.play(FadeIn(cards, shift=UP * 0.12), run_time=0.7)
        note = text("Entrevistas conserva el público joven; IELTS requiere dominio del examen y B2B cambia el comprador.", 15, MUTED)
        note.move_to(DOWN * 2.05)
        caveat = text("Compara ocupación, reservas pagadas y horas totales antes de cambiar tarifa.", 16, GOLD, BOLD)
        caveat.next_to(note, DOWN, buff=0.18)
        self.play(FadeIn(note), FadeIn(caveat), run_time=0.6)
        self.wait(7.9)
