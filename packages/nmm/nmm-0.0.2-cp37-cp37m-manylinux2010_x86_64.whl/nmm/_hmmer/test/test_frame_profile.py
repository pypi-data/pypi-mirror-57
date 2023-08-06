from numpy.testing import assert_allclose, assert_equal

from nmm import create_frame_profile, read_hmmer, GeneticCode


def test_frame_profile_frame1(PF03373):
    reader = read_hmmer(PF03373)
    hmmer = create_frame_profile(reader)

    # most_likely_seq = b"PGKEDNNK"
    most_likely_rna_seq = b"CCU GGU AAA GAA GAU AAU AAC AAA"
    most_likely_rna_seq = most_likely_rna_seq.replace(b" ", b"")

    r = hmmer.search(most_likely_rna_seq)
    assert_allclose(r.score, 125.83363182422178)
    frags = r.fragments
    assert_equal(len(frags), 1)
    frag = frags[0]
    assert_equal(frag.homologous, True)
    assert_equal(frag.sequence, most_likely_rna_seq)
    assert_equal(str(frag), "<FrameFragment:CCUGGUAAAGAAGAUAAUAACAAA>")


def test_frame_profile_frame2(PF03373):
    reader = read_hmmer(PF03373)
    hmmer = create_frame_profile(reader, epsilon=0.1)

    # seq = b"KKKPGKEDNNK"
    rna_seq = b"AAA AAA AAA CCU GGU AAA GAA GAU AAU AAC AAA"
    rna_seq = rna_seq.replace(b" ", b"")

    r = hmmer.search(rna_seq)
    assert_allclose(r.score, 168.23071232889802)
    frags = r.fragments
    assert_equal(len(frags), 2)
    assert_equal(frags[0].homologous, False)
    assert_equal(frags[0].sequence, b"AAAAAAAAA")
    assert_equal(frags[1].homologous, True)
    assert_equal(frags[1].sequence, b"CCUGGUAAAGAAGAUAAUAACAAA")


def test_frame_profile_frame3(PF03373):
    reader = read_hmmer(PF03373)
    hmmer = create_frame_profile(reader, epsilon=0.0)

    # seq = b"PGKEDNNK"
    rna_seq = b"CCU GGU AAA GAA GAU AAU AAC AAA"
    rna_seq = rna_seq.replace(b" ", b"")

    r = hmmer.search(rna_seq)
    frags = r.fragments
    assert_equal(len(frags), 1)
    assert_equal(frags[0].homologous, True)
    assert_equal(frags[0].sequence, b"CCUGGUAAAGAAGAUAAUAACAAA")


def test_frame_profile_frame4(PF03373):
    reader = read_hmmer(PF03373)
    hmmer = create_frame_profile(reader, epsilon=0.0)

    # seq = b"PGKEDNNK"
    rna_seq = b"CCUU GGU AAA GAA GAU AAU AAC AAA"
    rna_seq = rna_seq.replace(b" ", b"")

    r = hmmer.search(rna_seq)
    frags = r.fragments
    assert_equal(len(frags), 0)


def test_frame_profile_frame5(PF03373):
    reader = read_hmmer(PF03373)
    hmmer = create_frame_profile(reader, epsilon=0.00001)

    # seq = b"PGKEDNNK"
    rna_seq = b"CCUU GGU AAA GAA GAU AAU AAC AAA"
    rna_seq = rna_seq.replace(b" ", b"")

    r = hmmer.search(rna_seq)
    frags = r.fragments
    assert_equal(len(frags), 1)
    assert_equal(frags[0].homologous, True)
    assert_equal(frags[0].sequence, b"CCUUGGUAAAGAAGAUAAUAACAAA")


def test_frame_profile_frame6(PF03373):
    reader = read_hmmer(PF03373)
    hmmer = create_frame_profile(reader, epsilon=0.00001)

    # seq = b"PGKEDNNKEEPGKEDNNKEEE"
    rna_seq = b"CCUU GGU AAA GAA GAU AAU AAC AAA GAA GAA CCU GGU AAA GAA GAU AAU AAC AAA GAA GAA GA"
    rna_seq = rna_seq.replace(b" ", b"")

    r = hmmer.search(rna_seq)
    frags = r.fragments
    assert_equal(len(frags), 4)
    assert_equal(frags[0].homologous, True)
    assert_equal(frags[0].sequence, b"CCUUGGUAAAGAAGAUAAUAACAAA")
    assert_equal(frags[1].homologous, False)
    assert_equal(frags[1].sequence, b"GAAGAA")
    assert_equal(frags[2].homologous, True)
    assert_equal(frags[2].sequence, b"CCUGGUAAAGAAGAUAAUAACAAA")
    assert_equal(frags[3].homologous, False)
    assert_equal(frags[3].sequence, b"GAAGAAGA")

    hmmer.multiple_hits = False
    r = hmmer.search(rna_seq)
    frags = r.fragments
    assert_allclose(r.score, 1445.0314253859958)
    assert_equal(len(frags), 3)
    assert_equal(frags[0].homologous, False)
    assert_equal(frags[0].sequence, b"CCUUGGUAAAGAAGAUAAUAACAAAGAAGAA")
    assert_equal(frags[1].homologous, True)
    assert_equal(frags[1].sequence, b"CCUGGUAAAGAAGAUAAUAACAAA")
    assert_equal(frags[2].homologous, False)
    assert_equal(frags[2].sequence, b"GAAGAAGA")


def test_frame_profile_codons(PF03373):
    reader = read_hmmer(PF03373)
    hmmer = create_frame_profile(reader, epsilon=0.1)
    gcode = GeneticCode()

    # seq = b"KKKPGKEDNNK"
    rna_seq = b"AAGA AAA AAA CCU GGU AAA GAA GAU AAU AAC AAA G"
    rna_seq = rna_seq.replace(b" ", b"")

    r = hmmer.search(rna_seq)
    assert_allclose(r.score, 175.35113397356454)
    frags = r.fragments
    cfrags = [f.decode() for f in frags]
    aafrags = [f.decode(gcode) for f in cfrags]

    assert_equal(len(frags), 2)
    assert_equal(len(cfrags), 2)
    assert_equal(len(aafrags), 2)

    assert_equal(frags[0].homologous, False)
    assert_equal(cfrags[0].homologous, False)
    assert_equal(aafrags[0].homologous, False)
    assert_equal(frags[0].sequence, b"AAGAAAAAAA")
    assert_equal(cfrags[0].sequence, b"AAGAAAAAA")
    assert_equal(aafrags[0].sequence, b"KKK")

    items = list(frags[0].items())
    citems = list(cfrags[0].items())
    aaitems = list(aafrags[0].items())

    assert_equal(items[0][0], b"")
    assert_equal(str(items[0][1]), "<S,0>")
    assert_equal(citems[0][0], b"")
    assert_equal(str(citems[0][1]), "<S,0>")
    assert_equal(aaitems[0][0], b"")
    assert_equal(str(aaitems[0][1]), "<S,0>")

    assert_equal(items[1][0], b"AAG")
    assert_equal(str(items[1][1]), "<N,3>")
    assert_equal(citems[1][0], b"AAG")
    assert_equal(str(citems[1][1]), "<N,3>")
    assert_equal(aaitems[1][0], b"K")
    assert_equal(str(aaitems[1][1]), "<N,1>")

    assert_equal(items[2][0], b"AAAA")
    assert_equal(str(items[2][1]), "<N,4>")
    assert_equal(citems[2][0], b"AAA")
    assert_equal(str(citems[2][1]), "<N,3>")
    assert_equal(aaitems[2][0], b"K")
    assert_equal(str(aaitems[2][1]), "<N,1>")

    assert_equal(items[3][0], b"AAA")
    assert_equal(str(items[3][1]), "<N,3>")
    assert_equal(citems[3][0], b"AAA")
    assert_equal(str(citems[3][1]), "<N,3>")
    assert_equal(aaitems[3][0], b"K")
    assert_equal(str(aaitems[3][1]), "<N,1>")

    assert_equal(items[4][0], b"")
    assert_equal(str(items[4][1]), "<B,0>")
    assert_equal(citems[4][0], b"")
    assert_equal(str(citems[4][1]), "<B,0>")
    assert_equal(aaitems[4][0], b"")
    assert_equal(str(aaitems[4][1]), "<B,0>")

    assert_equal(frags[1].homologous, True)
    assert_equal(cfrags[1].homologous, True)
    assert_equal(aafrags[1].homologous, True)
    assert_equal(frags[1].sequence, b"CCUGGUAAAGAAGAUAAUAACAAAG")
    assert_equal(cfrags[1].sequence, b"CCUGGUAAAGAAGAUAAUAACAAG")
    assert_equal(aafrags[1].sequence, b"PGKEDNNK")

    items = list(frags[1].items())
    citems = list(cfrags[1].items())
    aaitems = list(aafrags[1].items())

    assert_equal(items[0][0], b"CCU")
    assert_equal(str(items[0][1]), "<M1,3>")
    assert_equal(citems[0][0], b"CCU")
    assert_equal(str(citems[0][1]), "<M1,3>")
    assert_equal(aaitems[0][0], b"P")
    assert_equal(str(aaitems[0][1]), "<M1,1>")

    assert_equal(items[7][0], b"AAAG")
    assert_equal(str(items[7][1]), "<M8,4>")
    assert_equal(citems[7][0], b"AAG")
    assert_equal(str(citems[7][1]), "<M8,3>")
    assert_equal(aaitems[7][0], b"K")
    assert_equal(str(aaitems[7][1]), "<M8,1>")
