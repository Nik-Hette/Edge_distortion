# Edge_distortion
Engine for creating console games.

#Module Properties:
- time_in_game - contains the number of repetitions of the main loop.
- game_state - contains the state of the game in a Boolean value.
- objects - contains an array with all entities 
- height- contains the height of the game world.
- width - contains the width of the game world.
- world - contains the matrix of the game world.
- skin_of_world - contains the texture of empty cells of the world.
- frame - contains textures of frames framing the game world.

#World
The world in the engine is a two-dimensional array. It is created using a sequence of two methods: init and creating_world.

##Methods for working with the world
- init (width, height) - changes the width and height of the world. This method must be used before the creating_world method.
- creating_world () - creates a matrix according to the height and width indicators
- clear () - cleans the world of entities.
- print_objects () - shows all entities from the objects array on the matrix.
- print_world () - outputs the matrix to the console.

#Entity
Within the framework of the engine, an entity is an object with a set of necessary properties and methods, which is located in the objects array. It is displayed on the screen as a symbol. 

Entity classes are stored in the main game file and are created from it using the new_object method. In order not to constantly prescribe mandatory properties, the Entity (x, y, t, skin) class was created, which has all the necessary properties. It should be designated as the parent of all entities.   

##required entity properties
- xy - coordinates of the entity on the canvas.
- t is the type of entity.
- number - index of the entity in the objects array.
- skin - texture (symbol) of the entity.

##methods for working with entities
- new_object (class ()) - adds an entity to the objects array.
- new_xy ([x, y], object number) - changes the coordinates of the entity.
- kill_all () - deletes all entities.
- kill_obj (object number) - deletes one entity.
- search_xy ([x, y]) - searches for an entity in the objects array and returns an array with the success of the search in a Boolean value, the type of entity, its number. 
- line ([x, y], [x, y], object) - creates a line from entities. The method is not able to work with horizontal lines.  
- square () - creates an empty square of entities.
- filled_square - creates a filled square of entities.
- upbating_obj - updates the sequence numbers of entities.

#Point
In the process of developing the engine, methods working directly with matrix cells (dots) were required. They are mostly used by other methods.

##Methods for working with points
- point ([x, y], skin) - changes the symbol on the matrix.
- kill_point - ([x, y]) - removes changes from the cell.
- line_xy ([x, y], [x, y]) - returns an array with coordinates of all points of the line.

#Touches
A feature of this engine is the ability to check the neighborhood of characters.

##Methods for working with touches
- checking_point ([x, y]) - returns information about the entity located at this point: type, coordinates, number. If there is no entity on the point, it will return Folse.
- checking_line ([x, y], [x, y], t) - returns an array with information about all entities of the specified type on the line. The array will contain nested arrays with coordinates and entity numbers. 
- checking_line_2 ([x, y], direction) - checks the line from a given point in a given direction and returns the type of the first entity encountered.
- checking_touch ([x, y]) - will screw in an array with checked neighboring points relative to the specified one. If there is no entity at the point, then there will be None in its place in the array.
- checking_filled ([x, y], [x, y], t) - returns an array with check points on a given full square.
- checking_square ([x, y], [x, y], t) - will screw in an array with checking points on a given floor square.

#Recommended structure of the main game file

- importing the engine
- entity classes
- level class
- control function
- Creating the World
- Creating a level
- game cycle:
- updating the world
- showing the world
- management
- Entity Cycle: 
- Entity Actions
- Checking for loss