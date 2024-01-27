import rospy
import smach

class ascent(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                outcomese=['init mapping', 'traversal', 'fail'],
                input_keys=['behavior'],
                output_keys=['behavior', 'target'])
                
    
    def execute (self, behavior):
        # extend linear actuators
        if True:
            return 'pass'
        else:
            return 'fail'
        
class init_mapping(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['pass', 'fail'],
                input_keys=['behavior'],
                output_keys=['behavior'])
    
    def execute (self, behavior):
        # sping 360 & find april tag & set target

        # generatte trajectory

        if True:
            return 'pass'
        else:
            return 'fail'
        
class traversal(smach.State):
    def __init__(self):
        smach.State.__inti__(self,
                outcomes=['target reached', 'detect robot stuck'],
                input_keys=['behavior&target'],
                output_keys=['behavior'])
        
    def execute (self, behavior, target):
        # generate trajectory

        # move along trajectory + recieve sensor input(imu, uwb, images) + update map

        if True:
            return 'target reached'
        else:
            return 'detect robot stuck'
        
class plunging(smach.Sate):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['pass', 'fail'],
                input_keys=['behavior'],
                output_keys=['behavior'])
    
    def execute (self, behavior):
        # Set excavation to full speed + lower 90% of distance

        # reduce speed to 25%

        if True:
            return 'pass'
        else:
            return 'fail'

class trenching(smach.Sate):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['load cell full', 'Obstacle reached', 'fail'],
                input_keys=['behavior'],
                output_keys=['behavior'])
    
    def execute (self, behavior):
        # drive forward + adjust speed

        if True:
            return 'pass'
        else:
            return 'fail'
        
class deposit(smach.Sate):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['load cell empty', 'fail':'FUCKED'],
                input_keys=['behavior'],
                output_keys=['behavior'])
    
    def execute (self, behavior):
        # spin auger

        # stop spinning auger

        if True:
            return 'pass'
        else:
            return 'fail'
        
class post_deposit(smach.Sate):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['pass', 'fail'],
                input_keys=['behavior'],
                output_keys=['behavior'])
    
    def execute (self, behavior):
        # shift future deposition location

        if True:
            return 'pass'
        else:
            return 'fail'
        
class escape(smach.Sate):
    def __init__(self):
        smach.State.__init__(self,
                outcomes=['back to traversal to mining',
                          'back to traversal to berm',
                          'detect robot stuck':'ESCAPE'],
                input_keys=['behavior'],
                output_keys=['behavior'])
    
    def execute (self, behavior):
        # drive stright at 100% speed

        if True:
            return 'pass'
        else:
            return 'fail'


def main():
    rospy.init_node('Lunabot behavior')

    sm_top = smach.StateMachine(outcomes = ['PASS', 'FAIL'])

    with sm_top:
        smach.StateMachine.add('ASCENT', ascent(), 
                                transitions={'init mapping':'INIT_MAPPING',
                                             'traversal to mining':'TRAVERSAL',
                                             'traversal to berm':'TRAVERSAL',
                                             'fail':'FUCKED'},
                                remapping={'input_keys' : 'behavior',
                                           'output_keys' : 'behavior&target'})
        
        smach.StateMachine.add('INIT_MAPPING', init_mapping(), 
                                transitions={'pass':'TRAVERSAL', 
                                             'fail':'FUCKED'},
                                remapping={'input_keys' : 'behavior',
                                           'output_keys' : 'behavior'})
        
        smach.StateMachine.add('TRAVERSAL', traversal(),
                                transitions={'target reached':'PLUGING',
                                            'detect robot stuck':'ESCAPE'},
                                remapping={'input_keys' : 'behavior&target',
                                           'output_keys' : 'behavior'})
        
        smach.StateMachine.add('PLUGING', plunging(), 
                                transitions={'pass':'TRENCHING', 
                                             'fail':'FUCKED'},
                                remapping={'input_keys' : 'behavior',
                                           'output_keys' : 'behavior'})
        
        smach.StateMachine.add('TRENCHING', trenching(), 
                                transitions={'load cell full':'ASCENT',
                                             'Obstacle reached':'ASCENT', 
                                             'fail':'FUCKED'},
                                remapping={'input_keys' : 'behavior',
                                           'output_keys' : 'behavior'})
        
        smach.StateMachine.add('DEPOSIT', deposit(), 
                                transitions={'load cell empty':'POST_DEPOSIT', 
                                             'fail':'FUCKED'},
                                remapping={'input_keys' : 'behavior',
                                           'output_keys' : 'behavior'})
        
        smach.StateMachine.add('POST_DEPOSIT', post_deposit(), 
                                transitions={'pass':'ASCENT', 
                                             'fail':'FUCKED'},
                                remapping={'input_keys' : 'behavior',
                                           'output_keys' : 'behavior'})
        
        smach.StateMachine.add('ESCAPE', escape(), 
                                transitions={'back to traversal to mining':'TRAVERSAL_TO_MINING',
                                             'back to traversal to berm':'TRAVERSAL_TO_BERM', 
                                             'detect robot stuck':'ESCAPE'},
                                remapping={'input_keys' : 'behavior',
                                           'output_keys' : 'behavior'})
        
    outcome = sm_top.execute()
        