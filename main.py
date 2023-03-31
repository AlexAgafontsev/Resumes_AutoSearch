from candidates_search.Sentence_Transformer import get_result

example_resumes = [
{   'id_resume': 1,
    'url': '1',
    'company': '',
    'position_name': 'Continuous optimization',
    'sentences': [
        'Nonlinear optimization',
        'Linear and nonlinear optimization.',
        'Linear and nonlinear optimization methods,',
        'Application of nonlinear optimization algorithms',
        'nonlinear optimization technique',
        'Proposing solutions based on mathematical optimization',
        'mathematical optimization',
        'processing using mathematical optimization algorithms',
        'Numerical Optimization',
    ],
        'sentence_vectors': [],
},

{   'id_resume': 1,
    'url': '1',
    'company': '',
    'position_name': 'Graphics Engine Specialist',
    'sentences': [
        'Computer graphics API: Vulkan, DX12',
        'Worked on postrocessing stack for rendering engine',
        'Implemented GPU skinning animation',
        'Developed Vulkan rendering engine for style applications',
        'Making offline rendering real-time on Radeon GPU',
        'I am a graphics software engineer in a highly-focused Graphics Performance Analyzers team dealing with the design and development of Intel GPA(R)',
        'computer graphics algorithms in one or more technical fields in physical simulation, rendering,3D-modeling, animation',
        'deep understanding of GPU rendering technology principles and performance optimization methods',
        'development of related technical algorithms such as graphics engine modeling, animation, rendering, physical simulation, material, and spatial calculation',
        'Development rendering engine',
        'Development of 3D tools for working with the model',
        'Modification of the used 3D engine to new requirements',
    ],
        'sentence_vectors': [],
},

{   'id_resume':1,
    'url': '1',
    'company': '',
    'position_name': 'Optical Modelling & Simulation Specialist',
    'sentences': [
        'optical modelling and simulation capability to support the development of ultra high precision optical system',
        'optical simualtion software and implementing relevant numerical simulation techniques.',
        'Matlab, Python or C++.',
        'industrial R&D scientist, physical modeling design engineer',
        'semiconductor optical metrology',
        'researching the fundamental diffraction physics of the light-matter interaction at the nanoscale',
        'image and signal formation physics of the optical sensors',
        'degree in theoretical physics, complemented of academic research experience in the field of fundamental precision measurements',
        'laser interferometric gravitational-wave observatories, and on quantum optomechanics with micromechanical oscillators',
        'classical optics and photonics',
        'optical coherence, aberration theory and imaging',
        'diffraction and scattering theory',
        'microscopy, scatterometry and polarimetry',
        'semiconductor and nanostructure metrology',
        'quantum mechanics and quantum optics',
        'laser interferometry and optomechanics',
        'electromagnetic and optics simulations',
        'general relativity and gravitational-wave theory',
        'MATLAB coding and software development',
        'numerical simulations studied several YieldStar sensor concepts for the future in-device metrology applications',
        'Developed an approximate but fully analytical model of diffraction of light by diffraction gratings, and of the overlay signal formation in metrology targets and semiconductor device structures',
        'The developed theory suggested novel overlay inference algorithms in both Fourier and image domains for various applications',
        ' numerical simulations studied the conceptual design options for the optical sensor aimed at boosting the accuracy, robustness and precision of in-device after-etch overlay measurements',
        'optical sensor for the future after-litho overlay metrology system',
        ' semiconductor metrology needs, created a high-level overview of the key challenges in optical overlay inspection, and compiled a short-list of potential hardware and algorithmic solutions',
        'studied the dynamical radiation pressure effects in optomechanical systems',
        'optomechanical dynamics which can be observed in small-scale systems (can be applied for e.g. testing quantum mechanics of macroscopic objects, and improving the sensitivity of micro-sensors)',
        'Developed a theoretical model for the table-top experiment on optomechanical cooling of a micromechanical oscillator',
        ' developed quantum noise reduction techniques (displacement-noise-free interferometry, speed-meter topology, etc.) for the 3rd-generation pan-European Einstein Telescope laser gravitational-wave observatory',
        'Developed a MATLAB program with GUI for statistical analysis of the data flow from the cosmic-rays detector hardware of a space satellite',
        'Mathematical and numerical modeling',
        'Development of a program in MATLAB that simulates heating of a three-dimensional body by laser radiation',
        'Modeling of optical processes.',
        'Fiber laser modeling.',
        'Simulation of pulse mode of laser operation at mode synchronization by saturating absorbers, method of nonlinear evolution of pulse polarization, acousto-optic modulation',
        'Mathematical modeling in optical systems',
        'Mathematical modeling, program Mir physical models',
    ],
        'sentence_vectors': [],
},


{   'id_resume':2,
    'url': '1',
    'company': '',
    'position_name': 'Optical Algorithm & Simulation Specialist',
    'sentences': [
        'build the optical algorithm & simulation capability to support the development of ultra high precision optical system',
        'computational mathematics, applied mathematics, physical optics, and computational optics',
        'knowledge of geometric, physical, and micronano optical systems, and have strong sequential, non-sequence, physical, and micronano optical modeling capabilities',
        'optical precision measurement algorithms, be familiar with FIR, FFT, and other signal processing knowledge, and have extensive experience in signal analysis and processing.',
        'numerical linear algebra, finite element, partial differential equation, large-scale matrix calculation, and solver',
        'optical simualtion software and implementing relevant numerical simulation techniques',
        'experience in light tracing, scalar or vector diffraction analysis, FDTD, FEM, and optical-related multi-physical-field coupling algorithms or software development',
        'parallel computing frameworks or environments such as OpenMP, MPI, CUDA, and OpenCL',
        'low temperature plasma devices (PVD systems, Hall-effect thrusters/ion sources, and dusty plasmas)',
        'Lead optical engineer for residual radiation management in laser-produced plasma-based EUV sources',
        'optical radiation load, glint, unwanted radiation towards scanne',
        'calculate EUV collection and shaping, laser radiation load, tracing of ballistic particles for contamination prevention',
        'creation of a complex multitool thermo-opto-mechanical model involving ANSYS, ZEMAX, Matlab, SigFit for CO2 laser beam quality in high power mirror system',
        'Matlab for complex simulation result post-processing and for analysis automation',
        'Matlab code for physical optics propagation-based calculation and merged it with Zemax ray tracing engine',
        'Performed various simulation and analysis tasks in the area of high-power IR and EUV light propagation in mirror systems',
        'LED-based illumination optics development (system design, simulation using TracePro and MATLAB)',
        'Development of algorithms for laser printer optics simulation tool',
        'research also in Atomic, Molecular and Optical Physics, Experimental Physics and Optics',
        'Research in the field of Atomic Physics, High Energy Physics, and Fundamental Symmetries',
        'optical engineers and laser scientists developing new technologies for high power lasers, beam delivery, focusing and steering in laser-produced plasma EUV source',
        'led technology development and demonstration of core laser system module enabling high volume EUV manufacturing and future power scaling',
        'major drive laser architectural change for LPP EUV source based on solid state laser systems',
        'implemented EUV source trigger emulator for stand-alone performance qualification of laser system',
        'Developed Matlab toolboxes for analysis of terabytes of EUV source performance data',
        'Led design, build, integration into an EUV sources and performance characterization of novel high-power seed systems based on CO2 MOPA laser architecture',
        'Built complex high power opto-mechanical breadboard systems',
        'laser system for immersion lithography',
        'excimer laser system for immersion lithography',
        'Created system performance breakdown, defined feasible changes for optical, controls, thermal, metrology subsystems ',
        'Optical information processing using nonlinear wave mixing with ultrashort pulse lasers. Heterodyne interferometry using femtosecond pulse lasers',
        'Professional experience in theoretical (physics, mathematics) and computational (mathematical modeling, computational methods)',
        'Development of numerical methods and coding of physical processes for engineering and scientific problems of numerical modeling',
        'Numerical modeling of processes: solid-state heating, process of absorption of laser radiation by a substance of study propagation in different media, diffraction phenomena taking into account the presence of aberrations of the radiation beam in the software package MATLAB.',
        'Formation and conduction of research in the field of laser physics, fiber lasers, interaction of laser radiation with substance',
        'Development and improvement of the mathematical core of the hydrodynamic simulator.',
        'Research of optical properties of materials.',
        'Design, assembly and testing of fiber-optic components, fiber lasers.',
        'Development of instruments and systems based on integrated optics.',
        'Analysis of Mir trends in photonics and integrated optics to prepare proposals for further work.',
    ],
        'sentence_vectors': [],
},



{   'id_resume':3,
    'url': '1',
    'company': '',
    'position_name': 'Radiation Hydrodynamics modeling and simulation  architect',
    'sentences': [
        'radiation hydrodynamics modeling and simulation relating to laser-plasma interactions or discharge-plasma interaction, with profound studies on laser ablation',
        'raidation transport and hydrodynamics, plasma spatiotemporal evolution and resulted recoil presure, and abilitiy of experimental data analysis and modeling validation',
        'Deliver high presicion and high robustness modeling and simulation codes by applying accurate equation of state and opacity data table, resonable assumptions of the complex physical mechanisms, accurate boundary condition difinitions and numerical methods into the simulation architecture',
        'plasma physics, radiation hydrodynamics, liquid hydrodynamics',
        'code writing experience on laser-induced plasma, laser ablation, radiation transport and hydrodynamics',
        'running modeling and simulation of radiation hydrodynamics programs',
        'use of data analysis tools such as Fortran, C++, Matlab, Python',
        'Mathematical & computer modeling',
        'Plasma dynamics modeling',
        'Computation of atomic processes in plasma',
        'EUV and soft X-ray sources modelling',
        'Research of fluid dynamics and conductive fluid dynamics',
        'Fluid dynamo modelling',
        'Fluid dynamics computation',
        'Research and computation of influence of atomic processes in plasma',
        'Computation of atomic processes in non-equilibrium plasma',
        'Plasma surface interaction and optics lifetime',
        'Specialties: X-ray EUV optics, X-ray tomography, multilayer mirrors, X-ray microscopy',
        'Computational methods in the field of high-temperature plasma physics.',
        'numerical modeling of processes in plasma',
        'work in the field of laser-plasma interaction, development of numerical models of physical processes',
    ],
        'sentence_vectors': [],
},
]


def print_comands():
    print('Выбери и напиши свой вариант ответа(цифра которая указана под каждой командой, введи ее и нажми enter',
              '1-Начать работу программы', '2-Нужна помощь', '3-Описание программы', '4-Для других разработчиков', sep='\n')
    print('press enten to exit')

    message = input()
    if message:
        try:
            answer = int(message)
        except:
            return
    else:
        return
    if answer == 1:
        print('Начнем!')
        print('Введи пожалуйста название файла, лучше не повторяться, чтобы не мешать другим!')
        filename = input()
        print('Убедитесь что вы вставили все нужные предложения в список example_resumes который находиться в самом верху файла,',
              'если что перезапустите работу програмы', sep='\n')
        get_result(example_resumes, filename)
    if answer == 2:
        print('Мои контакты:', 'Телефон', '89049166729', 'telegram', 'https://t.me/AgafontsevSasha', sep='\n')
    if answer == 3:
        print('Это программа по поиску релевантных кандидатов на основе предложений, из резюме которые уже приняли')
    if answer == 4:
        print('asd')
    print('press enter to exit')
    exit = input()
    if exit == '':
        print_comands()



def start():
    print('Привет!', 'Это краткая инструкция, как пользоваться программой по поиску кандидатов',
              'Для начала поймем что тебе нужно', sep='\n')
    print_comands()



if __name__ == '__main__':
    start()