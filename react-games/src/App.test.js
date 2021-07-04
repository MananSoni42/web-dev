import React from 'react'
import { shallow } from 'enzyme'

import Connect4 from './connect4'
import UltimateTicTacToe from './ultimate_ttt'

describe('Connect 4 Component', () => {
    it('should render correctly', () => {
        const component = shallow(<Connect4 />)
        expect(component).toHaveLength(1)
    })
})

describe('Ultimate TTT 4 Component', () => {
    it('should render correctly', () => {
        const component = shallow(<UltimateTicTacToe />)
        expect(component).toHaveLength(1)
    })
})
