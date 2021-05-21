from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)
from kivy.vector import Vector
from kivy.clock import Clock



class PongEndMsg(Widget):
    displayText = StringProperty("")
    button = ObjectProperty(None)


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    # Kivy objects
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    pongEndMsg = None

    # Game variables
    ball_velocity = (10, 0)
    gameIsCurrentlyOn = True

    def start_the_game(self):
        self.gameIsCurrentlyOn = True
        self.serve_ball()

    def serve_ball(self, vel=(10, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        if self.gameIsCurrentlyOn:
            self.ball.move()

            # bounce of paddles
            self.player1.bounce_ball(self.ball)
            self.player2.bounce_ball(self.ball)

            # bounce ball off bottom or top
            if (self.ball.y < self.y) or (self.ball.top > self.top):
                self.ball.velocity_y *= -1

            # went of to a side to score point?
            if self.ball.x < self.x:
                self.player2.score += 1
                self.serve_ball(vel=self.ball_velocity)
            if self.ball.x > self.width:
                self.player1.score += 1
                self.serve_ball(vel=(-self.ball_velocity[0], self.ball_velocity[1]))

            # check for game over and ask to restart the game
            if self.player1.score == 3 or self.player2.score == 3:
                self.gameIsCurrentlyOn = False
                self.remove_widget(self.player1)
                self.remove_widget(self.player2)
        else:
            # display that someone won
            if self.pongEndMsg is None:
                self.pongEndMsg = PongEndMsg()
                self.pongEndMsg.center = self.center
                self.pongEndMsg.displayText = "Player {id} has won!".format(id=1 if self.player1.score == 3 else 2)
                self.pongEndMsg.button.bind(on_press=self.restart_game)
                self.add_widget(self.pongEndMsg)
            pass

    def on_touch_move(self, touch):
        if self.gameIsCurrentlyOn:
            if touch.x < self.width / 2.1:
                self.player1.center_y = touch.y
            if touch.x > self.width - self.width / 2.1:
                self.player2.center_y = touch.y

    def restart_game(self, instance):
        self.add_widget(self.player1)
        self.add_widget(self.player2)
        self.remove_widget(self.pongEndMsg)

        self.pongEndMsg = None
        self.player1.score = 0
        self.player2.score = 0
        self.serve_ball(vel=self.ball_velocity)
        self.gameIsCurrentlyOn = True


class PongApp(App):
    def build(self):
        game = PongGame()
        game.start_the_game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


class ProjectPage(Widget):

    def update(self, dt):
        pass

    def on_touch_move(self, touch):
        pass

class SimpleTamagochiApp(App):
    def build(self):
        projectPage = ProjectPage()
        Clock.schedule_interval(projectPage.update, 1.0 / 60.0)
        return projectPage


if __name__ == '__main__':
    SimpleTamagochiApp().run()