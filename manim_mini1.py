from manim import *
import numpy as np
#whenever you want to test the animation, copy paste this: python -m manim manim_mini1.py Test
class Test(Scene):
    def construct(self):
        title = Text("Radio Signals: AM vs FM", font_size=48) #title text here
        subtitle = Text("By Alex Terhakopian", font_size=28).next_to(title, DOWN) #subtitle text here
        self.add_sound(
            "audio/Part1.mp3",
            gain=1.25,        # Volume adjustment
            time_offset=1  # Delay start by 0.5 seconds
        )
        self.play(Write(title), run_time=1.5) #run time is adjustable 
        self.play(FadeIn(subtitle, shift=DOWN), run_time=1.5)
        self.wait(6) #how long it is paused 

        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.75) #now a fade out 
        self.wait(1)
        ##above this is the title animation: it fully works and is synced with audio. Audio is part 1 
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": WHITE},
        )
    
        sin_wave = axes.plot(
            lambda x: np.sin(x),
            color=BLUE,
            x_range=[0, 4 * PI],
        )
        self.wait(0.1)
        self.add_sound("audio/Part2.mp3", gain=1.25) #uadio here ###########  python -m manim manim_mini1.py Test
        self.play(Create(axes), run_time=1)
        self.play(Create(sin_wave), run_time=2)

        #Amplitude annotation (4 seconds in)
        self.wait(2.5)  # 1s wait + 2s create + 1s axes = ~4s

        amplitude_line = axes.plot_line_graph(
            x_values=[PI / 2, PI / 2],
            y_values=[0, 1],
            line_color=YELLOW,
            add_vertex_dots=False,
        )
        amplitude_label = Text("Amplitude", font_size=28, color=YELLOW).next_to(
            axes.c2p(PI / 2, 1), RIGHT
        )
        amplitude_brace = Brace(amplitude_line, direction=RIGHT, color=YELLOW)

        self.play(Create(amplitude_brace), Write(amplitude_label), run_time=1)

        #Frequency annotation (3 seconds later)
        self.wait(2)  # pad to ~3s gap

        frequency_brace = BraceBetweenPoints(
            axes.c2p(0, -1.7),
            axes.c2p(2 * PI, -1.7),
            direction=DOWN,
            color=GREEN,
        )
        frequency_label = Text("1 Cycle (Frequency)", font_size=28, color=GREEN).next_to(
            frequency_brace, DOWN
        )

        self.play(Create(frequency_brace), Write(frequency_label), run_time=1)
        self.wait(6)#potentially change this, see what it is like tmr 
        #part 2 is done, audio is fully in sync. ###########  python -m manim manim_mini1.py Test
        # Clear previous section
        self.play(
            FadeOut(axes),
            FadeOut(sin_wave),
            FadeOut(amplitude_brace),
            FadeOut(amplitude_label), #####clear 
            FadeOut(frequency_brace),
            FadeOut(frequency_label),
            run_time=1
        )

        #Message Signal
        message_title = Text("Message Signal", font_size=48).to_edge(UP, buff=0.3) 
        self.play(Write(message_title), run_time=1)

        axes_msg = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": WHITE},
        ).move_to(ORIGIN)

        message_wave = axes_msg.plot(
            lambda x: np.sin(2 * x),
            color=BLUE,
            x_range=[0, 4 * PI],
        )

        self.play(Create(axes_msg), Create(message_wave), run_time=2)
        self.wait(1) ######################################################## timing stamp, so it can be changed to fit audio 

        #Message formula (4 seconds in)
        msg_formula = MathTex(
            r"m(t) = 1 + 0.5\sin(2\pi f_m t)",
            font_size=32
        ).to_edge(DOWN, buff=0.4)

        self.play(Write(msg_formula), run_time=1)
        self.wait(3) ######################################################## timing stamp, so it can be changed to fit audio 

        #Clear everything
        self.play(
            FadeOut(message_title),
            FadeOut(axes_msg),
            FadeOut(message_wave),
            FadeOut(msg_formula),
            run_time=1
        )
        #Carrier Signal
        carrier_title = Text("Carrier Signal", font_size=48).to_edge(UP, buff=0.3)
        self.play(Write(carrier_title), run_time=1)

        axes_carrier = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": WHITE},
        ).move_to(ORIGIN)

        carrier_wave = axes_carrier.plot(
            lambda x: np.sin(4 * x),
            color=BLUE,
            x_range=[0, 4 * PI],
        )

        self.play(Create(axes_carrier), Create(carrier_wave), run_time=2)
        self.wait(5)

        # Carrier formula (4 seconds in) 
        carrier_formula = MathTex(
            r"f_c \geq 2f_m",
            font_size=32
        ).to_edge(DOWN, buff=0.4)

        self.play(Write(carrier_formula), run_time=1)
        self.wait(7)

        # Clear everything ################################################# python -m manim manim_mini1.py Test (code to copy past to test)
        self.play(
            FadeOut(carrier_title),
            FadeOut(axes_carrier),
            FadeOut(carrier_wave),
            FadeOut(carrier_formula),
            run_time=1
        )
        ################################ animation functions. Audio NOT added. Continual issues in doing so / serious unrelaibility on behalf of manim          
        # Amplitude Modulation 
        am_title = Text("Amplitude Modulation", font_size=48).to_edge(UP, buff=0.3)
        self.play(Write(am_title), run_time=1)

        axes_am = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": WHITE},
        ).move_to(ORIGIN)

        fm = 2
        fc = 20

        am_wave = axes_am.plot(
            lambda t: (1 + 0.5 * np.sin(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t),
            color=YELLOW,
            x_range=[0, 4 * PI],
        )

        self.play(Create(axes_am), Create(am_wave), run_time=2)
        self.wait(1)

        #AM formula (4 seconds in) 
        am_formula = MathTex(
            r"\text{AM Signal} = m(t) \times c(t)",
            font_size=32
        ).to_edge(DOWN, buff=0.4)

        self.play(Write(am_formula), run_time=1)
        self.wait(5)

        #Clear everything #######################################python -m manim manim_mini1.py Test
        #self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1) #ERROR HERE!!! it clears everything out. When I tried to fix it more errors occured in line 125-170 which is very wierd
        #self.play(    
        #    FadeOut(am_title),
        #    FadeOut(am_wave,
        #    FadeOut(am_formula),
        #    run_time=1)
        #)
        # AM Decoding 
        am_decode_title = Text("AM Decoding", font_size=48).to_edge(UP, buff=0.3)
        self.play(Write(am_decode_title), run_time=1)

        #Formula first 
        decode_formula = Text("Take Absolute Value", font_size=32).to_edge(DOWN, buff=0.4)
        self.play(Write(decode_formula), run_time=1)
        self.wait(5)###############################################################################

        #Absolute value wave (4 seconds in) 
        axes_decode = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": WHITE},
        ).move_to(ORIGIN)

        fm = 2
        fc = 20

        decode_wave = axes_decode.plot(
            lambda t: np.abs((1 + 0.5 * np.sin(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)),
            color=ORANGE,
            x_range=[0, 4 * PI],
        )

        self.play(Create(axes_decode), Create(decode_wave), run_time=2)
        self.wait(2)

        #Clear everything ######################################## python -m manim manim_mini1.py Test
        self.play(
            FadeOut(am_decode_title),
            FadeOut(axes_decode),
            FadeOut(decode_wave),
            FadeOut(decode_formula),
            run_time=1
        )
        #Moving Average 
        new_formula = Text("Take Moving Average", font_size=32).to_edge(DOWN, buff=0.4)
        self.play(Transform(decode_formula, new_formula), run_time=1)

        # overlay the envelope (moving average approximation)
        envelope_wave = axes_decode.plot(
            lambda t: (1 + 0.5 * np.sin(2 * np.pi * fm * t)),
            color=RED,
            x_range=[0, 4 * PI],
        )

        self.play(Create(envelope_wave), run_time=2)
        self.wait(2)

        #Clear everything 
        self.play(
            FadeOut(am_decode_title),
            FadeOut(axes_decode),
            FadeOut(decode_wave),
            FadeOut(decode_formula),
            FadeOut(envelope_wave),
            run_time=1
        )