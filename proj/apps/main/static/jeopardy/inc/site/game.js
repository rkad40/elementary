var selectedCategories = [];
var passCode = '7342';
var exitCode = '7883';
var allCategories = [
    // Young Sheldon
    {
        title: 'Young Sheldon <i class="fas fa-atom"></i>',
        questions: [
            {
                value: 2,
                answer: "Young Sheldon a spin-off of this show.",
                questions: [
                    '(A) What is <i>Hannah Montana</i>?',
                    '(B) What is <i>How I Met Your Mother</i>?',
                    '(C) What is <i>The Big Bang Theory</i>?',
                    '(D) What is <i>George and Mandy\'s First Marriage?</i>',
                ],
                correct: 'C',
            },
            {
                value: 3,
                answer: "The university that Sheldon Cooper attends at the end of the show.",
                questions: [
                    '(A) What is Caltech?',
                    '(B) What is MIT?',
                    '(C) What is Harvard?',
                    '(D) What is Stanford?',
                ],
                correct: 'A',
            },
            {
                value: 4,
                answer: 'Sheldon attempts to protect his lunch in the school refrigerator by doing this.',
                questions: [
                    '(A) What is by labeling it "Radioactive Materials"?',
                    '(B) What is by disguising it as a milk carton?',
                    '(C) What is by booby-trapping it with an ink bomb.',
                    '(D) What is by putting a radio tracker in his sandwich?',
                ],
                correct: 'A',
            },
            {
                value: 5,
                answer: 'The name of the comic book store Sheldon frequents.',
                questions: [
                    '(A) What is Galaxy Comics?',
                    '(B) What is King\'s Comic Cavern?',
                    '(C) What is Grant\'s Comic Emporium?',
                    '(D) What is Atomic Comics?',
                ],
                correct: 'B',
            },
        ]
    },

    // Napoleon Dynamite
    {
        title: 'Napoleon Dynamite <i class="fa fa-video"></i>',
        questions: [
            {
                value: 2,
                answer: "What Pedro promises students who vote for him to be president.",
                questions: [
                    '(A) What is "I will put vending machines in the cafeteria"?',
                    '(B) What is "I offer you protection"?',
                    '(C) What is "All your wildest dreams will come true"?',
                    '(D) What is "I will shave my head"?',
                ],
                correct: 'C',
            },
            {
                value: 3,
                answer: "The name of Napoleon\'s grandma\'s pet lama.",
                questions: [
                    '(A) What is Starla?',
                    '(B) What is Tina?',
                    '(C) What is Deb?',
                    '(D) What is Sandy?',
                ],
                correct: 'B',
            },
            {
                value: 4,
                answer: 'The name of the girl that reluctantly goes to the school dance with Napoleon.',
                questions: [
                    '(A) Who is Deb?',
                    '(B) Who is Summer?',
                    '(C) Who is Trisha?',
                    '(D) Who is Lafawnduh?',
                ],
                correct: 'C',
            },
            {
                value: 5,
                answer: 'The cost of Rex\'s eight week class in "Rex Kwon Do".',
                questions: [
                    '(A) What is $50?',
                    '(B) What is $99?',
                    '(C) What is $199?',
                    '(D) What is 300?',
                ],
                correct: 'D',
            },
        ]
    },

    // The State of Texas
    {
        title: 'The Great State of Texas <i class="fas fa-flag"></i>',
        questions: [
            {
                value: 2,
                answer: 'Texas city that is home to the Johnson Space Center.',
                questions: [
                    '(A) What is Dallas?',
                    '(B) What is San Antonio?',
                    '(C) What is Houston?',
                    '(D) What is Austin?',
                ],
                correct: 'C',
            },
            {
                value: 3,
                answer: 'This is Texas\' state rank in land mass size among the 50 U.S. states.',
                questions: [
                    '(A) What is first?',
                    '(B) What is second?',
                    '(C) What is third?',
                    '(D) What is fourth?',
                ],
                correct: 'B',
            },
            {
                value: 4,
                answer: 'This U.S. state shares the longest border with Texas.',
                questions: [
                    '(A) What is New Mexico?',
                    '(B) What is Oklahoma?',
                    '(C) What is Arkansas?',
                    '(D) What is Louisiana?',
                ],
                correct: 'B',
            },
            {
                value: 5,
                answer: 'This U.S. President was born in Texas.',
                questions: [
                    '(A) Who is Dwight D Eisenhower?',
                    '(B) Who is John F. Kennedy?',
                    '(C) Who is George W. Bush?',
                    '(D) who is George H. Bush?',
                ],
                correct: 'A',
            },
        ]
    },

    // 80's Rock Bands
    {
        title: '80\'s Rock Bands <i class="fas fa-guitar"></i>',
        questions: [
            {
                value: 2,
                answer: 'This band sang the the hit song "All I Wanna Do Is Make Love to You".',
                questions: [
                    '(A) Who are the Eagles?',
                    '(B) Who is the Bangles?',
                    '(C) Who is Madonna?',
                    '(D) Who is Heart?',
                ],
                correct: 'D',
            },
            {
                value: 3,
                answer: 'In their hit song, this band lamented, "Everybody wants to rule the world".',
                questions: [
                    '(A) Who is Def Leopard?',
                    '(B) Who is Journey?',
                    '(C) Who is Survivor?',
                    '(D) Who is Tears for Fears?',
                ],
                correct: 'D',
            },
            {
                value: 4,
                answer: 'This individual was the lead vocalist for the band "Queen".',
                questions: [
                    '(A) Who is Prince?',
                    '(B) Who is Sting?',
                    '(C) Who is Freddie Mercury?',
                    '(D) Who is Brett Michaels?',
                ],
                correct: 'C',
            },
            {
                value: 5,
                answer: 'Michael Jackson was the top selling rock artist in the 80\'s. This artist was second.',
                questions: [
                    '(A) Who is Madonna?',
                    '(B) Who is U2?',
                    '(C) Who is Prince?',
                    '(D) Who is Bon Jovi?',
                ],
                correct: 'A',
            },
        ]
    },

    // Netflix Series
    {
        title: 'Netflix Series <i class="fas fa-tv"></i>',
        questions: [
            {
                value: 2,
                answer: 'This Netflix series is set in the 1980\'s and features a group of kids facing supernatural forces.',
                questions: [
                    '(A) What is <i>Emily in Paris</i>?',
                    '(B) What is <i>Bridgerton</i>?',
                    '(C) What is <i>Outer Banks</i>?',
                    '(D) What is <i>Stranger Things</i>?',
                ],
                correct: 'D',
            },
            {
                value: 3,
                answer: 'This Netflix series chronicles the reign of Queen Elizabeth II in England.',
                questions: [
                    '(A) What is <i>Queen\'s Gambit</i>?',
                    '(B) What is <i>The Crown</i>?',
                    '(C) What is <i>Young Royals</i>?',
                    '(D) What is <i>The Queen</i>?',
                ],
                correct: 'B',
            },
            {
                value: 4,
                answer: 'This 2022 Netflix series features the true story of Erick and Lyle Menendez who were convicted in 1996 of killing their parents.',
                questions: [
                    '(A) What is <i>Monsters</i>?',
                    '(B) What is <i>Evil Down the Hall</i>?',
                    '(C) What is <i>No One Will Suspect Us</i>?',
                    '(D) What is <i>Ingratitude</i>?',
                ],
                correct: 'A',
            },
            {
                value: 5,
                answer: 'This actor plays Uncle Fester in Netflix\'s hit series <i>Wednesday</i>.',
                questions: [
                    '(A) Who is Katherine Zeta-Jones?',
                    '(B) Who is Luis Guzman?',
                    '(C) Who is Fred Armisen?',
                    '(D) Who is Steve Buscemi?',
                ],
                correct: 'C',
            },
        ]
    },

    // The U.S. in World War II
    {
        title: 'The U.S. in World War II <i class="fas fa-flag-usa"></i>',
        questions: [
            {
                value: 2,
                answer: 'The United States entered WWII after the Japanese conducted a successful sneak attack on this U.S. base.',
                questions: [
                    '(A) What is Fort Hood?',
                    '(B) What is Okinawa?',
                    '(C) What is Camp Pendleton?',
                    '(D) What is Pearl Harbor?',
                ],
                correct: 'D',
            },
            {
                value: 3,
                answer: 'The battle in which U.S. led forced invaded Nazi occupied Europe by beach landing.',
                questions: [
                    '(A) What is the Battle of Guadalcanal?',
                    '(B) What is the Battle of Normandy?',
                    '(C) What is the Battle of the Bulge?',
                    '(D) What is the Battle of Midway?',
                ],
                correct: 'B',
            },
            {
                value: 4,
                answer: 'The main battle tank of the United States during World War II.',
                questions: [
                    '(A) What is the M1 Abrams?',
                    '(B) What is the M4 Sherman?',
                    '(C) What is the M60 Patton?',
                    '(D) What is the M551 Sheridan?',
                ],
                correct: 'B',
            },
            {
                value: 5,
                answer: 'The TV series <i>Band of Brothers</i> featured the 506th battalion from this prestigious unit.',
                questions: [
                    '(A) What is the 1st Cavalry Division?',
                    '(B) What is 1st Ranger Battalion?',
                    '(C) What is 101st Airborne Division?',
                    '(D) What is 82nd Airborne Division?',
                ],
                correct: 'C',
            },
        ]
    },

    // The Bible
    {
        title: 'The Bible <i class="fas fa-book-bible"></i>',
        questions: [
            {
                value: 2,
                answer: 'This is the very first book of the Bible.',
                questions: [
                    '(A) What is Revelation?',
                    '(B) What is the Gospel of John?',
                    '(C) What is Leviticus?',
                    '(D) What is Genesis?',
                ],
                correct: 'D',
            },
            {
                value: 3,
                answer: 'This city is identified in the Bible as the place where Jesus was born.',
                questions: [
                    '(A) What is Jerusalem?',
                    '(B) What is Nazareth?',
                    '(C) What is Bethlehem?',
                    '(D) What is Capernaum?',
                ],
                correct: 'C',
            },
            {
                value: 4,
                answer: 'This is the first King of Israel mentioned in the Old Testament.',
                questions: [
                    '(A) Who is David?',
                    '(B) Who is Saul?',
                    '(C) Who is Solomon?',
                    '(D) Who is Josiah?',
                ],
                correct: 'B',
            },
            {
                value: 5,
                answer: 'This New Testament book includes Jesus\' famous Sermon on the Mount.',
                questions: [
                    '(A) What is the Gospel of Matthew?',
                    '(B) What is the Gospel of Mark?',
                    '(C) What is the Gospel of Luke?',
                    '(D) What is the Gospel of John?',
                ],
                correct: 'A',
            },
        ]
    },

    // The Night Sky
    {
        title: 'The Night Sky <i class="fas fa-moon"></i>',
        questions: [
            {
                value: 2,
                answer: 'This star remains relatively fixed above the north pole and was used in ancient times for navigation.',
                questions: [
                    '(A) What is Antares?',
                    '(B) What is Sirius A?',
                    '(C) What is Vega?',
                    '(D) What is the North Star?',
                ],
                correct: 'D',
            },
            {
                value: 3,
                answer: 'Ancient astronomers called these "wandering stars" because they moved against the backdrop of stationary stars.',
                questions: [
                    '(A) What are the planets?',
                    '(B) What is the Big Dipper?',
                    '(C) What are comets?',
                    '(D) What is the sun and moon?',
                ],
                correct: 'A',
            },
            {
                value: 4,
                answer: 'Outside of our own sun, this is the closest star to Earth in the night sky, at about 4.2 light years in distance.',
                questions: [
                    '(A) What is Betelgeuse (a.k.a. Beetlejuice)?',
                    '(B) What is Proxima Centauri?',
                    '(C) What is Regulus?',
                    '(D) What is Selusa Secundus?',
                ],
                correct: 'B',
            },
            {
                value: 5,
                answer: 'Discovered in 2017, this asteroid is known as the "the first confirmed interstellar object to pass through our solar system". It displayed unexplained acceleration when leaving our system, some even suggesting it might be a an alien craft.',
                questions: [
                    '(A) What is Hale–Bopp?',
                    '(B) What is Oumuamua?',
                    '(C) What is Shoemaker–Levy 9?',
                    '(D) What is Apophis?',
                ],
                correct: 'B',
            },
        ]
    },

];

