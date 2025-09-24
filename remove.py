import re

# Provided text
text = """Aconite (Monkshood)
Ageratum
Allium
Alstroemeria (Peruvian Lily)
Amaryllis
Anemone
Angelonia
Anthurium
Aster
Azalea
Baby's Breath (Gypsophila)
Bachelor's Button (Centaurea)
Begonia
Bellflower (Campanula)
Bergenia
Bird of Paradise (Strelitzia)
Bleeding Heart (Lamprocapnos)
Bluebell (Hyacinthoides)
Bougainvillea
Buttercup (Ranunculus)
Calendula (Pot Marigold)
Calla Lily (Zantedeschia)
Camellia
Canna Lily
Carnation (Dianthus)
Chrysanthemum
Clematis
Clivia
Columbine (Aquilegia)
Coneflower (Echinacea)
Coreopsis
Cosmos
Crocus
Cyclamen
Daffodil (Narcissus)
Dahlia
Daisy (Bellis perennis)
Delphinium
Dianthus
Dutch Iris
Echinacea (Coneflower)
Edelweiss (Leontopodium)
Erica (Heath)
Euphorbia
Freesia
Fuchsia
Gaillardia (Blanket Flower)
Gardenia
Gazania
Geranium (Pelargonium)
Gerbera Daisy
Gladiolus
Goldenrod (Solidago)
Heather (Calluna)
Hellebore (Christmas Rose)
Hibiscus
Hollyhock (Alcea)
Honeysuckle (Lonicera)
Hyacinth
Hydrangea
Impatiens
Iris
Ivy (Hedera - grown for flowers)
Jasmine
Joe-Pye Weed (Eutrochium)
Jonquil (Narcissus)
Kaffir Lily (Clivia)
Kalanchoe
Kangaroo Paw (Anigozanthos)
Knapweed (Centaurea)
Lantana
Larkspur (Consolida)
Lavender
Lilac (Syringa)
Lily (Lilium)
Lily of the Valley (Convallaria)
Lobelia
Lotus (Nelumbo)
Lupine (Lupinus)
Magnolia
Marigold (Tagetes)
Mimosa
Monkshood (Aconitum)
Morning Glory (Ipomoea)
Mums (Chrysanthemum)
Narcissus (Daffodil)
Nasturtium
Nemesia
Nicotiana (Flowering Tobacco)
Nigella (Love-in-a-Mist)
Oleander
Orchid
Osteospermum (African Daisy)
Oxeye Daisy (Leucanthemum vulgare)
Pansy (Viola wittrockiana)
Passion Flower (Passiflora)
Peony
Petunia
Phlox
Pincushion Flower (Scabiosa)
Poppy (Papaver)
Primrose (Primula)
Protea
Queen Anne's Lace (Daucus carota - Wild Carrot)
Quince (Flowering - Chaenomeles)
Ranunculus
Rhododendron
Rose
Rosemary (flowers)
Rudbeckia (Black-Eyed Susan)
Salvia (Sage)
Snapdragon (Antirrhinum)
Snowdrop (Galanthus)
Statice (Limonium)
Stephanotis
Stocks (Matthiola)
Sunflower (Helianthus)
Sweet Pea (Lathyrus odoratus)
Tulip
Tansy
Thrift (Armeria)
Tiger Lily (Lilium lancifolium)
Trillium
Tuberose
Ursinia
Utricularia (Bladderwort - aquatic flower)
Verbena
Viola
Violet (Viola sororia)
Wallflower (Erysimum)
Water Lily (Nymphaea)
Wisteria
Xeranthemum (Immortelle)
Xylobium (Orchid genus)
Xyris (Yellow-Eyed Grass)
Yarrow (Achillea)
Yellow Archangel (Lamium galeobdolon)
Yellowhorn (Xanthoceras sorbifolium)
Yucca (flowers)
Zinnia
Zantedeschia (Calla Lily)
Zenobia
Zephyranthes (Rain Lily)
Acacia
Ageratum
Amaryllis
Anemone
Anthurium
Arbutus
Aster
Azalea
Baby’s-breath
Bachelor’s button
Belladonna
Bindweed
Blazing star
Bougainvillea
Broom
Buttercup
Calla (Calla Lily)
Camellia
Candytuft
Canna
Canterbury bell
Caper
Carnation
Chrysanthemum
Coreopsis
Crocus
Cyclamen
Daffodil
Dahlia
Daisy
Dandelion
Day lily
Easter lily
Eucalyptus
Everlasting
Flax
Forget-me-not
Forsythia
Foxglove
Gardenia
Gentian
Geranium
Gladiolus
Goldenrod
Heath
Heliotrope
Hibiscus
Hollyhock
Honeysuckle
Hyacinth
Hydrangea
Iris
Indian Paintbrush
Indigofera
Ipomea (Morning Glory)
Jasmine
Jonquil
Kerria
Kalanchoe
Lady’s slipper
Larkspur
Lavender
Lilac
Lily
Lily of the valley
Lotus
Magnolia
Marigold
Mimosa
Mint (Flowering)
Mistletoe
Monkey Flower
Morning Glory
Mountain Laurel
Mullein
Mustard
Myrtle
Narcissus
Nasturtium
Nigella
Night Jasmine
Oleander
Orchid
Oxalis
Pansy
Passionflower
Peony
Periwinkle
Petunia
Phlox
Poinsettia
Poppy
Protea
Primrose
Quince
Queen Anne’s lace
Rhododendron
Rose
Rose of Sharon
Safflower
Sage
Snowbell
Snapdragon
Sunflower
Sweet pea
Thistle
Trillium
Tuberose
Tulip
Ulex (Gorse)
Utricularia (Bladderwort)
Verbena
Viburnum
Violet
Water lily
Wisteria
Xanthoceras
Xeranthemum
Yarrow
Yucca
Zinnia
Acacia
Acanthus
Aconite
African Daisy (Dimorphotheca pluvialis)
African Violet (Saintpaulia)
Allium
Alstroemeria
Amaranth
Amaryllis
Anemone
Angelonia
Anthurium
Aster
Astilbe
Azalea
Baby's Breath
Bachelor's Button
Balloon Flower
Balsam
Begonia
Bellflower
Bird of Paradise
Black-Eyed Susan
Bleeding Heart
Bluebell
Bougainvillea
Broom
Buttercup
Calendula
Calla Lily
Camellia
Candytuft
Canna Lily
Canterbury Bells
Carnation
Celosia
Cherry Blossom
Chrysanthemum
Clematis
Cockscomb
Coneflower
Coral Bells
Coreopsis
Cornflower
Cosmos
Crocus
Daffodil
Dahlia
Daisy
Dandelion
Daylily
Delphinium
Dianthus
Dogwood
Edelweiss
Elephant Ear Flower
Evening Primrose
Feverfew
Flax
Forget-Me-Not
Foxglove
Freesia
Fuchsia
Gaillardia
Gardenia
Geranium
Gerbera Daisy
Gladiolus
Globe Thistle
Goldenrod
Grape Hyacinth
Hawthorn
Helenium
Heliconia
Hellebore
Hibiscus
Hollyhock
Honeysuckle
Hosta
Hyacinth
Hydrangea
Impatiens
Indian Paintbrush
Iris
Jacob's Ladder
Jasmine
Kangaroo Paw
King Protea
Lantana
Lavender
Lilac
Lily
Lily of the Valley
Lisianthus
Lobelia
Lotus
Lupine
Magnolia
Mallow
Marigold
Milkweed
Mimosa
Morning Glory
Myrtle
Nasturtium
Nicotiana
Oleander
Orchid
Pansy
Passion Flower
Peony
Petunia
Phlox
Pincushion Flower
Poppy
Primrose
Queen Anne's Lace
Quince
Ranunculus
Rhododendron
Rose
Rose of Sharon
Rosemary
Salvia
Snapdragon
Snowdrop
Spirea
Statice
Stephanotis
Stock
Sunflower
Sweet Pea
Sweet William
Teasel
Thistle
Tiger Lily
Trillium
Tuberose
Tulip
Verbena
Veronica
Vinca
Violet
Wallflower
Water Lily
Wisteria
Yarrow
Zinnia"""

# Remove all text within parentheses along with the parentheses
cleaned_text = re.sub(r"\s*\([^)]*\)", "", text)

cleaned_text[:1000]  # show first part to verify

print(cleaned_text)