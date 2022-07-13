import { revertString } from './revertString.js'

describe('test to reverse string', () => {
    it('expecting back reverse string', () => {
        expect(revertString('string')).toBe("gnirts")
    })
})
