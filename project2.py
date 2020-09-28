import arcade
#Owen Lafont
def main ():

    arcade.open_window(800, 800, "Rocketship")
    arcade.set_background_color(arcade.color.AFRICAN_VIOLET)


    arcade.start_render()


    rocketship_body = arcade.create_rectangle(200,300,100,100, arcade.color.ALMOND)

    thruster = arcade.create_p



    rocketship_body.draw()




    arcade.finish_render()
    arcade.run()
main()